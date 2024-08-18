from peewee import Model, CharField, DateTimeField
from db.database import db
import datetime

class Customer(Model):
    name = CharField()
    email = CharField()
    createdAt = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
