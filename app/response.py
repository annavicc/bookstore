from flask import Response
from flask_restplus_marshmallow import Api


class CustomResponse(Response):
    default_mimetype = 'application/json'


class CustomApi(Api):
    default_mediatype = 'application/json'

    def render_doc(self):
        response = super().render_doc()
        return response, 200, {
            'Content-Type': 'text/html'
        }
