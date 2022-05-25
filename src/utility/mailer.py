from flask_mail import Mail, Message
from src import create_app
from src.config.config import config_dict

app = create_app(config=config_dict['development'])
# # integrate Flask Mail
mail = Mail(app=app)


def send_mail(data):
    """
    Function to send emails.
    """
    with app.app_context():
        msg = Message(subject=data['title'],
                      sender="admin.ping",
                      recipients=[data['email']])
        msg.body = data['message']
        mail.send(msg)
