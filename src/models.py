from email.policy import default
from flask_mongoengine import MongoEngine
from datetime import datetime

# instantiate mongodb
db = MongoEngine()


class User(db.Document):
    username = db.StringField(max_length=20, required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    # messages = db.ReferenceField(Message)

    def __repr__(self):
        return "User >>> {self.username}"


class DurationUnit(db.EnumField):
    MINUTES = 'minutes'
    HOURS = 'hours'
    DAYS = 'days'


class Message(db.Document):
    title = db.StringField(max_length=50, required=True)
    body = db.StringField()
    duration = db.IntField(required=True)
    duration_unit = db.EnumField(DurationUnit, default=DurationUnit.MINUTES)
    user = db.ReferenceField(User)

    def __repr__(self):
        return "Title >>> {self.title}"
