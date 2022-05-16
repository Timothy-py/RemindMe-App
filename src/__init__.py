
# ####################################################################################

from flask import Flask, jsonify

# ####################################################################################


def create_app():
    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    # API Index Route
    @app.route('/')
    def index():
        return jsonify({
            'message': 'RemindMe App',
            'description': 'A Flask App that allow users to set reminders that will be delivered to their emails at a set time.'
        })

    return app


# mongodb+srv://Timothy:<password>@cluster0.db0z1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
