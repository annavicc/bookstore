from flask_restplus import fields


class ClientFields(object):

    def __init__(self, api):
        self.api = api
        self.client_json = {
            'id': fields.String(),
            'name': fields.String()
        }

    def output(self):
        return self.api.model('Client', self.client_json)

    def input(self):
        client = self.client_json.copy()
        del client['id']
        return self.api.model('ClientData', client)
