from re import M
from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.models import User, Message


# configure message Route
message = Blueprint('message', __name__, url_prefix='/api/message')


# ############################################################################
# send message API
@message.post('/')
@jwt_required()
def send_message():
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

    # instantiate a new message object
    new_message = Message(
        title=title,
        body=message,
        duration=duration,
        user=user_id
    ).save()

    return jsonify(message='Message scheduled successfully.'), 201
