from celery import Celery
from flask import Flask
from flask_mail import Mail, Message

from ...config import config_dict

app = Flask(__name__)
config = config_dict['development']
app.config.from_object(config)

# integrate Flask Mail
mail = Mail(app=app)

# setup celery client
client = Celery(app.name, broker=config.CELERY_BROKER_URL)
client.conf.update(app.config)


@client.task
def send_mail(data):
    """
    Function to send emails.
    """
    with app.app_context():
        msg = Message(subject=data['title'],
                      recipients=[data['email']])
        msg.body = data['message']
        mail.send(msg)
