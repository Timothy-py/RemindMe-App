
# ####################################################################################

from flask import Flask, jsonify
from ..config import config_dict
from mongoengine import connect
from .auth import auth
from .message import message
from flask_jwt_extended import JWTManager
# ####################################################################################


def create_app(config=config_dict['development']):
    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    # connect the database - mongodb
    connect(host=config.DB_HOST)
    # db.app = app
    # db.init_app(app)

    # initialize JWT Manager
    JWTManager(app=app)

    # register app handlers
    app.register_blueprint(auth)
    app.register_blueprint(message)

    # API Index Route
    @app.route('/')
    def index():
        return jsonify({
            'message': 'RemindMe App',
            'description': 'A Flask App that allow users to set reminders that will be delivered to their emails at a set time.'
        })

    return app