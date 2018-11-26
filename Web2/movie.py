from mongoengine import Document, StringField, IntField

class Movie(Document):
    title = StringField()
    image = StringField()
    year = IntField()
