'''
    Book endpoints
'''
from flask import request
from flask_restplus import Namespace, Resource
from .models import Book
from .serializers import BookFields, ReservationFields
from ..clients.models import Client
from ..exceptions import BookReservedError, NotFoundError


book_ns = Namespace('books', description='Book operations')
book_input = BookFields(book_ns).input()
book_output = BookFields(book_ns).output()
reservation_input = ReservationFields(book_ns).input()
reservation_output = ReservationFields(book_ns).output()


@book_ns.route('/', endpoint='book-controller')
class BookController(Resource):

    @book_ns.marshal_list_with(book_output)
    def get(self):
        return list(Book.objects())

    @book_ns.marshal_with(book_output, code=201)
    @book_ns.expect(book_input, validate=True)
    def post(self):
        book = Book(**request.json)
        book.save()
        return book, 201


@book_ns.route('/<id>/reserve', endpoint='reservation-controller')
class ReservationController(Resource):

    @book_ns.marshal_with(reservation_output, code=201)
    @book_ns.expect(reservation_input, validate=True)
    def post(self, id):
        req = request.json
        try:
            book = Book.objects().get(id=id)
            client = Client.objects.get(id=req['client_id'])
            reservation = book.reserve(client)
        except Book.DoesNotExist:
            return NotFoundError('book').abort_message()
        except Client.DoesNotExist:
            return NotFoundError('client').abort_message()
        except BookReservedError as err:
            return err.abort_message()
        return reservation
