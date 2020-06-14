from mongoengine import connect, disconnect
from app.clients.models import Client
from app.books.models import Book, Reservation


def setup_module(module):
    ''' Set up method to connect with a mocked db '''
    connect('mongoenginetest', host='mongomock://localhost')


def teardown_module(module):
    ''' Teardown connection '''
    disconnect()


class TestClient:
    def test_save_client(self):
        name = 'Anna'

        client = Client(name=name)
        client.save()

        result = Client.objects(name=name).first()
        assert result.name == name
        assert result.id is not None
        client.delete()

    def test_get_reserved_books(self):
        title = 'Book 1'
        price = 20.99
        book = Book(title=title, price=price)
        book.save()
        name = 'Anna'
        client = Client(name=name)
        client.save()
        expected = book.reserve(client)

        reservation = Reservation.objects.get(id=expected.id)
        assert reservation.client == client
        assert reservation.book == book
        assert reservation.total_price == book.price
