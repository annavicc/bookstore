from datetime import datetime, timedelta
from mongoengine import Document, StringField, \
    FloatField, DateField, ReferenceField
from ..clients.models import Client
from ..exceptions import BookReservedError
from ..enums import AVAILABLE, RESERVED


class Book(Document):
    title = StringField(required=True)
    price = FloatField(required=True)
    status = StringField(default=AVAILABLE)

    def reserve(self, client):
        if self.status == RESERVED:
            raise BookReservedError
        reservation = Reservation(date_reserved=datetime.now(),
                                  client=client,
                                  book=self,
                                  total_price=self.price)
        self.status = RESERVED
        reservation.save()
        self.save()
        return reservation


class Reservation(Document):
    client = ReferenceField(Client, required=True)
    book = ReferenceField(Book, required=True)
    date_reserved = DateField(required=True)
    date_returned = DateField()
    total_price = FloatField()

    def update_price(self):
        self.total_price = round(self.get_total_price(), 2)
        self.save()

    def get_total_price(self):
        additional_price = self.get_additional_price()
        return self.book.price + additional_price

    def get_additional_price(self):
        max_date = self.date_reserved + timedelta(days=3)
        today = datetime.now().date()
        fine = 0
        interest_rate = 0
        original_price = self.book.price
        if today <= max_date:
            return fine
        days = abs((today - max_date).days)
        if days < 3:
            fine = 0.03
            interest_rate = 0.002
        elif days >= 3 and days <= 4:
            fine = 0.05
            interest_rate = 0.004
        else:
            fine = 0.07
            interest_rate = 0.006
        return original_price * fine + interest_rate * days * original_price
