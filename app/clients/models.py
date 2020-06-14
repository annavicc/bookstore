from mongoengine import Document, StringField


class Client(Document):
    name = StringField(required=True)
