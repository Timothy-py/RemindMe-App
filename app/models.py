# from flask_mongoengine import MongoEngine
from datetime import datetime
from mongoengine import StringField, EmailField, DateTimeField, ReferenceField, Document, IntField, CASCADE
from marshmallow import Schema, fields, validate

# instantiate mongodb
# db = MongoEngine()


class User(Document):
    username = StringField(max_length=20, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    # messages = db.ReferenceField(Message)

    def __repr__(self):
        return "User >>> {self.username}"


class UserSchema(Schema):
    id = fields.Str()
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class Message(Document):
    title = StringField(max_length=50, required=True)
    body = StringField()
    start_datetime = DateTimeField(default=datetime.utcnow)
    duration = IntField(required=True)
    # user = ReferenceField('User', reverse_delete_rule=CASCADE)
    user = ReferenceField(User)

    def __repr__(self):
        return "Title >>> {self.title}"


class MessageSchema(Schema):
    id = fields.Str()
    title = fields.Str(required=True)
    body = fields.Str(required=True)
    start_datetime = fields.DateTime(required=True)
    duration = fields.Int(required=True)
    duration_unit = fields.Str(
        required=True, validate=validate.OneOf(['minutes', 'hours', 'days']))
    # user = fields.Nested("User")
