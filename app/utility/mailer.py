from celery import Celery
from flask import Flask
from flask_mail import Mail, Message

# import app as application
from ..models import Message as Msg
from .logger import logger
from config import config_dict

application = Flask(__name__)
config = config_dict['development']
application.config.from_object(config)

# integrate Flask Mail
mail = Mail(app=application)

# setup celery client
client = Celery(application.name, broker=config.CELERY_BROKER_URL,
                backend=config.RESULT_BACKEND)
client.conf.update(application.config)


@client.task(name='Mailer')
def send_mail(data):
    """
    Function to send emails.
    """

    with application.app_context():
        msg = Message(subject=data['title'],
                      recipients=[data['email']])
        msg.body = data['message']
        mail.send(msg)
        logger.info(
            f"Scheduled message by user - {data['email']} sent successfully")
        # update message status
        Msg.objects(id=data['id']).update_one(set__status='SUCCEEDED')


# Celery.control.revoke(
#     [scheduled["request"]["id"] for scheduled in chain.from_iterable(
#         Celery.control.inspect().scheduled().itervalues())]
# )
