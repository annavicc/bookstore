import os
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from app.routers import load_routes
from app.response import CustomResponse, CustomApi as Api
from flask_marshmallow import Marshmallow

APP = Flask(__name__)
CORS(APP, resources={r'/*': {'origins': '*'}})
DB_URI = "mongodb+srv://{}:{}@{}".format(
    os.environ['DB_USER'],
    os.environ['DB_PASS'],
    os.environ['DB_HOST']
)
APP.config["MONGODB_HOST"] = DB_URI
MongoEngine(APP)

APP.config['JSON_SORT_KEYS'] = False
Marshmallow(APP)
APP.response_class = CustomResponse
api = Api(
    app=APP,
    default_mediatype='application/json',
    title="Bookstore"
)
load_routes(api)


if __name__ == '__main__':
    api.run()
