# ############################################################
from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from flask_jwt_extended import create_access_token, create_refresh_token

from .models import User


# configure authentication Route
auth = Blueprint('auth', __name__, url_prefix='/api/auth')

# ############################################################


# API parameters validator function
def validator(username, email, password):
    error = []

    # validate the payloads
    if len(password) < 6:
        error.append("Password too short")

    if len(username) < 3:
        error.append("Username too short")

    if not username.isalnum() or " " in username:
        error.append(
            'Username should not contain spaces and non-alphanumeric character')

    if not validators.email(email):
        error.append('Email is not valid')

    return error


# ############################################################################
# user signup api
@auth.post('/signup')
def signup():
    # retrieve payloads from request body
    body = request.get_json()
    # username = request.json['username']
    # email = request.json['email']
    # password = request.json['password']

    # validate payloads
    error = validator(**body)
    # error = validator(username, email, password)

    if len(error) > 0:
        return jsonify({
            'error': error
        }), 400

    # check if the user exist in the db
    if User.objects(email=body['email']).first() is not None:
        return make_response(jsonify({
            'error': "User already exist",
        }), 409)

    # encryp the password string
    password_hash = generate_password_hash(body['password'])

    # instantiate a new user object
    new_user = User(**body)
    new_user.password = password_hash
    # new_user = User(
    #     email=email,
    #     username=username,
    #     password=password_hash
    # )

    # save to db
    new_user = new_user.save()

    return make_response(jsonify({
        'message': 'User registered successfully'
    }), 200)
# ############################################################################


# ############################################################################
# User signin API
@auth.post('/signin')
def signin():
    # retrieve payloads from request body
    email = request.json['email']
    password = request.json['password']

    # query the db for the email=user
    user = User.objects(email=email).first()
    if user is None:
        return make_response(jsonify({
            'error': 'Invalid User'
        }), 404)

    # check if password is correct
    password_correct = check_password_hash(user.password, password)

    # if password is not correct
    if password_correct == False:
        return make_response(jsonify({
            'error': 'Incorrect password'
        }), 401)

    # generate token
    access_token = create_access_token(identity=user.email)
    refresh_token = create_refresh_token(identity=user.email)
    # send OK response
    return make_response(jsonify({
        'message': 'Logged in successfully',
        'user': {
            'username': user.username,
            'email': email,
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    }), 200)
