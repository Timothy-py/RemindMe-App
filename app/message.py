from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from .models import Message
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

    # retrieve payloads from request body
    title = request.json['title']
    message = request.json['body']
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
    data['email'] = user_id

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
