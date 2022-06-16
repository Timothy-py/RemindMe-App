
# ####################################################################################

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from mongoengine import connect
from flasgger import Swagger, swag_from

from config import config_dict
from swagger import template, swagger_config
from .auth import auth
from .message import message
# ####################################################################################


def create_app(config=config_dict['development']):
    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    # connect the database - mongodb
    connect(host=config.DB_HOST)

    # initialize JWT Manager
    JWTManager(app=app)

    # register app handlers
    app.register_blueprint(auth)
    app.register_blueprint(message)

    # configure swagger
    Swagger(app=app, config=swagger_config, template=template)

    # API Index Route
    @app.route('/')
    @swag_from('./docs/index.yaml')
    def index():
        return jsonify({
            'message': 'RemindMe App',
            'description': 'A Flask App that allow users to set reminders that will be delivered to their emails at a set time.'
        }), 200

    return app
