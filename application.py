import datetime
import logging
import os
import time

from flask import Response, request

from src.PickEmLeague import create_app

application = create_app(os.getenv("FLASK_ENV", "development"))
application.logger.setLevel(logging.DEBUG)


@application.route("/")
def index():
    return f'The index page {os.getenv("FLASK_ENV", "development")}'


@application.before_request
def log_request_start():
    # print(f"{datetime.datetime.fromtimestamp(time.time())}: {request.url}")
    pass


@application.after_request
def log_request_end(response: Response):
    # print(f"{datetime.datetime.fromtimestamp(time.time())}: {response.json}")
    return response


if __name__ == "__main__":
    application.run()
