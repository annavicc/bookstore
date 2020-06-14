'''
    Client endpoints
'''
from flask import request
from flask_restplus import Namespace, Resource
from .models import Client
from .serializers import ClientFields
from ..books.models import Reservation
from ..books.serializers import ReservationFields
from ..enums import RESERVED


client_ns = Namespace('client', description='Clients operations')
client_input = ClientFields(client_ns).input()
client_output = ClientFields(client_ns).output()
reservation_output = ReservationFields(client_ns).output()


@client_ns.route('/', endpoint='clients-controller')
class ClientsController(Resource):

    @client_ns.marshal_list_with(client_output, code=200)
    def get(self):
        return list(Client.objects())

    @client_ns.marshal_with(client_output, code=201)
    @client_ns.expect(client_input, validate=True)
    def post(self):
        client = Client(**request.json)
        client.save()
        return client, 201


@client_ns.route('/<id>/books', endpoint='reserved-controller')
class ReservedBooksController(Resource):

    @client_ns.marshal_with(reservation_output, code=200)
    def get(self, id):
        reservations = Reservation.objects(client=id)
        active = list(filter(
                        lambda r: r.book.status == RESERVED,
                        reservations)
                      )
        list(map(lambda r: r.update_price(), active))
        return active
