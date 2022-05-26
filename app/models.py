# from flask_mongoengine import MongoEngine
from datetime import datetime
from mongoengine import StringField, EmailField, DateTimeField, ReferenceField, Document, IntField

# instantiate mongodb
# db = MongoEngine()


class User(Document):
    username = StringField(max_length=20, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    # messages = db.ReferenceField(Message)

    def __repr__(self):
        return "User >>> {self.username}"


# class DurationUnit(db.EnumField):
#     MINUTES = 'minutes'
#     HOURS = 'hours'
#     DAYS = 'days'


class Message(Document):
    title = StringField(max_length=50, required=True)
    body = StringField()
    start_datetime = DateTimeField(default=datetime.utcnow)
    duration = IntField(required=True)
    user = ReferenceField(User)

    def __repr__(self):
        return "Title >>> {self.title}"
