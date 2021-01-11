from flask import Flask
from flask_mongoengine import MongoEngine
from config import config
from .routes import *


def create_app():
    app = Flask(__name__)
    app.config["MONGODB_SETTINGS"] = config
    db = MongoEngine(app)
    app.register_blueprint(routes)

    return app
    