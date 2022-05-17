
# ####################################################################################

from flask import Flask, jsonify
from .config.config import config_dict
from src.models import db
from src.auth import auth

# ####################################################################################


def create_app(config=config_dict['development']):
    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    # connect the database - mongodb
    db.app = app
    db.init_app(app)

    # register app handlers
    app.register_blueprint(auth)

    # API Index Route
    @app.route('/')
    def index():
        return jsonify({
            'message': 'RemindMe App',
            'description': 'A Flask App that allow users to set reminders that will be delivered to their emails at a set time.'
        })

    return app
