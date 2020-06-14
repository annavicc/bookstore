from datetime import datetime
from mongoengine import connect, disconnect
from app.books.models import Book
from app.clients.models import Client
from app.enums import RESERVED, AVAILABLE

CLIENT = 'Anna'


def setup_module(module):
    ''' Set up method to connect with a mocked db '''
    connect('mongoenginetest', host='mongomock://localhost')
    client = Client(name=CLIENT)
    client.save()


def teardown_module(module):
    ''' Teardown connection '''
    disconnect()


class TestBook:

    def test_save_book(self):
        title = 'Book 1'
        price = 20.99

        book = Book(title=title, price=price)
        book.save()

        result = Book.objects(title=title).first()
        assert result.title == title
        assert result.id is not None
        assert result.price == price
        assert result.status == AVAILABLE
        book.delete()

    def test_reserve_book(self):
        title = 'Book 1'
        price = 20.99

        book = Book(title=title, price=price)
        book.save()

        client = Client.objects(name=CLIENT).first()
        reservation = book.reserve(client)

        assert book.status == RESERVED
        assert reservation.client == client
        assert reservation.date_reserved == datetime.now().date()
