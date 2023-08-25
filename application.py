import datetime
import logging
import os
import time
from logging.config import dictConfig

import colors
from flask import Response, g, request

from src.PickEmLeague import create_app

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "worldClock.log",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)

application = create_app(os.getenv("FLASK_ENV", "development"))
application.logger.setLevel(logging.DEBUG)


@application.route("/")
def index():
    return f'The index page {os.getenv("FLASK_ENV", "development")}'


@application.before_request
def log_request_start():
    print(f"{datetime.datetime.fromtimestamp(time.time())}: {request.url}")


@application.after_request
def log_request_end(response: Response):
    print(f"{datetime.datetime.fromtimestamp(time.time())}: {response.json}")
    return response


if __name__ == "__main__":
    application.run()
