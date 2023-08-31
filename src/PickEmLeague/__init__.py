"""Flask app initialization via factory pattern."""
import datetime
import logging
import os
import time

import colors
import flask_migrate
from flask import Flask, g, request
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.PickEmLeague.config import get_config

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def configure_logging():
    # register root logging
    logging.basicConfig(level=logging.DEBUG)
    # logging.getLogger("werkzeug").setLevel(logging.INFO)


def create_app(config_name):
    configure_logging()
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_object(get_config(config_name))
    # configure_logging()

    from src.PickEmLeague.apis import api_bp

    application.register_blueprint(api_bp, url_prefix="/api")

    cors.init_app(application)
    db.init_app(application)
    migrate.init_app(application, db, directory="src/PickEmLeague/migrations")
    bcrypt.init_app(application)

    with application.app_context():
        flask_migrate.upgrade(directory="src/PickEmLeague/migrations")

    @application.before_request
    def before():
        print("Factory app before request")

    @application.errorhandler(Exception)
    def error(e):
        print("Error")

    return application
