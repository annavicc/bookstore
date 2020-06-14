from flask_restplus import fields
from ..clients.serializers import ClientFields

class BookFields(object):

    def __init__(self, api):
        self.api = api
        self.book_json = {
            'id': fields.String(),
            'title': fields.String(),
            'price': fields.Float(),
            'status': fields.String()
        }

    def output(self):
        return self.api.model('Book', self.book_json)

    def input(self):
        book = self.book_json.copy()
        del book['id']
        return self.api.model('BookData', book)


class ReservationFields(object):

    def __init__(self, api):
        self.api = api
        self.res_json = {
            'id': fields.String(),
            'book': fields.Nested(self.api.model(
                                    'BookData',
                                    BookFields(self.api).output())
                                  ),
            'client': fields.Nested(self.api.model(
                                        'ClientData',
                                        ClientFields(self.api).output()
                                    )),
            'total_price': fields.Float(),
            'date_reserved': fields.Date(),
            'date_returned': fields.Date()
        }

    def input(self):
        res = self.res_json.copy()
        del res['id']
        del res['date_reserved']
        del res['date_returned']
        return self.api.model('ReservationData', res)

    def output(self):
        return self.api.model('Reservation', self.res_json)
