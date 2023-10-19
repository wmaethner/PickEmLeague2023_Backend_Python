"""Flask app initialization via factory pattern."""
import datetime
import logging
import os
import time

import colors
import flask_migrate
from flask import Flask, g, request
from flask_apscheduler import APScheduler
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.PickEmLeague.config import get_config

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
scheduler = APScheduler()


def auto_task():
    jobs = scheduler.get_jobs()
    print("task executed")
    print(jobs)


def create_app(config_name):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_object(get_config(config_name))

    from src.PickEmLeague.apis import api_bp
    from src.PickEmLeague.services.tasks import daily_game_check

    application.register_blueprint(api_bp, url_prefix="/api")

    cors.init_app(application)
    db.init_app(application)
    migrate.init_app(application, db, directory="src/PickEmLeague/migrations")
    bcrypt.init_app(application)
    scheduler.init_app(application)

    scheduler.start()

    # scheduler.add_job(
    #     "date_task",
    #     auto_task,
    #     trigger="date",
    #     run_date=datetime.datetime(2023, 10, 15, 21, 11, 10),
    # )

    scheduler.add_job(
        "date_task_local",
        auto_task,
        trigger="date",
        run_date=datetime.datetime(2023, 10, 15, 17, 11, 50),
    )

    with application.app_context():
        flask_migrate.upgrade(directory="src/PickEmLeague/migrations")

    # @scheduler.task(
    #     "date",
    #     id="upcoming_game_check",
    #     run_date=datetime.datetime(2023, 9, 15, 21, 1, 0),
    # )
    # def scheduled_task():
    #     jobs = scheduler.get_jobs()
    #     print("task executed")
    #     print(jobs)

    # @scheduler.task("interval", id="test", seconds=10)
    # def interval_task():
    #     jobs = scheduler.get_jobs()
    #     print(jobs)
    #     print(f"Interval: {datetime.datetime.now()}")
    #     print(f"Interval: {datetime.datetime.utcnow()}")

    return application
