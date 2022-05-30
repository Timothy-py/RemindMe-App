from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# integrate Flask Mail
mail = Mail(app=app)


def send_mail(data):
    """
    Function to send emails.
    """
    with app.app_context():
        msg = Message(subject=data['title'],
                      recipients=[data['email']])
        msg.body = data['message']
        mail.send(msg)
