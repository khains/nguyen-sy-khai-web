from mongoengine import Document, StringField, IntField, BooleanField

class River(Document):
    meta = {
        "strict" : False
    }
    name = StringField()
    continent = StringField()
    length = IntField()
    available = BooleanField(default=False)