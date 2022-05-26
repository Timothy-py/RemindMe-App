from flask_mail import Mail, Message

from ... import wsgi


# integrate Flask Mail
mail = Mail(app=wsgi.app)


def send_mail(data):
    """
    Function to send emails.
    """
    with wsgi.app.app_context():
        msg = Message(subject=data['title'],
                      sender="admin.ping",
                      recipients=[data['email']])
        msg.body = data['message']
        mail.send(msg)
