from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from .models import Message, MessageSchema, User, UserSchema
from .utility.mailer import send_mail

# configure message Route
message = Blueprint('message', __name__, url_prefix='/api/message')


# ############################################################################
# send message API
@message.post('/')
@jwt_required()
@swag_from('./docs/message/send_message.yaml')
def send_message():
    data = {}
    # get Logged in user id
    user_id = get_jwt_identity()
    # >>>>>>>>>>>>>validate requesst body>>>>>>>>>>>>>

    # query the db for the user=user_id
    user = User.objects(id=user_id).first()

    serializer = UserSchema()
    user_data = serializer.dump(user)

    # retrieve payloads from request body
    title = request.json['title']
    message = request.json['message']
    duration_unit = request.json['duration_unit']
    duration = request.json['duration']

    if duration_unit == 'minutes':
        duration *= 60
    elif duration_unit == 'hours':
        duration *= 3600
    elif duration_unit == 'days':
        duration *= 86400

    data['title'] = title
    data['message'] = message
    data['email'] = user_data['email']

    # send mail Function
    send_mail.apply_async(args=[data], countdown=duration)

    # instantiate a new message object
    Message(
        title=title,
        body=message,
        duration=duration,
        user=user_id
    ).save()

    return jsonify(message='Message scheduled successfully.'), 201


# ############################################################################
# fetch my messages
@message.get('/')
@jwt_required()
@swag_from('./docs/message/fetch_message.yaml')
def fetch_message():
    # get Logged in user
    user_id = get_jwt_identity()

    try:
        messages = Message.objects(user=user_id).all()

        serializer = MessageSchema(many=True)

        data = serializer.dump(messages)

    except Exception as error:
        return jsonify({
            'message': 'An error occured',
            'error': error
        }), 500

    else:
        return make_response(jsonify({
            'message': 'All your messages fetched successfully',
            'data': data
        }), 200)
