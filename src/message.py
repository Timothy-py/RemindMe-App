from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.models import User, Message, db


# configure message Route
message = Blueprint('message', __name__, url_prefix='/api/message')


# ############################################################################
# send message API
@message.post('/message')
@jwt_required()
def message():
    data = {}
    # get Logged in user id
    user_id = get_jwt_identity()
    print(user_id)
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

    # load data object
    data['title'] = title
    data['message'] = message
    data['user'] = user_id

    return make_response(jsonify({data}), 200)
