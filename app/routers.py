'''
    Blueprints
'''
from app.books.controllers import book_ns
from app.clients.controllers import client_ns


def load_routes(application):
    application.add_namespace(book_ns)
    application.add_namespace(client_ns)
