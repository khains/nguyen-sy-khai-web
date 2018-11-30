from mongoengine import Document, StringField, IntField

class Register(Document):
    username = StringField()
    password = StringField()
    email = StringField()
