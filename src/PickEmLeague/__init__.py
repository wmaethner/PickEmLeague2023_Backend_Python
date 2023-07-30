"""Flask app initialization via factory pattern."""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.PickEmLeague.config import get_config

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(get_config(config_name))

    from src.PickEmLeague.apis import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db, directory="src/PickEmLeague/migrations")
    bcrypt.init_app(app)
    return app
