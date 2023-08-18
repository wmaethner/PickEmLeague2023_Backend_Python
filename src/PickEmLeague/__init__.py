"""Flask app initialization via factory pattern."""
import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy

from src.PickEmLeague.config import get_config

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_name):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_object(get_config(config_name))

    from src.PickEmLeague.apis import api_bp

    application.register_blueprint(api_bp, url_prefix="/api")

    cors.init_app(application)
    db.init_app(application)
    migrate.init_app(application, db, directory="src/PickEmLeague/migrations")
    bcrypt.init_app(application)

    with application.app_context():
        upgrade(directory="src/PickEmLeague/migrations")

    return application
