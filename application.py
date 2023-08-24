import datetime
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


@application.route("/")
def index():
    return f'The index page {os.getenv("FLASK_ENV", "development")}'


@application.before_request
def log_request_start():
    print(f"{datetime.datetime.fromtimestamp(time.time())}: {request.url}")
    # if request.method == "GET":
    #     if request.args:
    #         print(request.args)
    #         print(len(request.args))
    # elif request.method == "POST":
    #     print(request.form)


@application.after_request
def log_request_end(response: Response):
    print(f"{datetime.datetime.fromtimestamp(time.time())}: {response.json}")
    return response


@application.errorhandler
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    print(e)
    # start with the correct headers and status code from the error
    # response = e.get_response()
    # replace the body with JSON
    # response.data = json.dumps(
    #     {
    #         "code": e.code,
    #         "name": e.name,
    #         "description": e.description,
    #     }
    # )
    # response.content_type = "application/json"
    # return response


# @application.before_request
# def start_timer():
#     g.start = time.time()


# @application.after_request
# def log_request(response):
#     if request.path == "/favicon.ico":
#         return response
#     elif request.path.startswith("/static"):
#         return response

#     now = time.time()
#     duration = round(now - g.start, 2)
#     dt = datetime.datetime.fromtimestamp(now)

#     # timestamp = rfc3339(dt, utc=True)

#     ip = request.headers.get("X-Forwarded-For", request.remote_addr)
#     host = request.host.split(":", 1)[0]
#     args = dict(request.args)

#     log_params = [
#         ("method", request.method, "blue"),
#         ("path", request.path, "blue"),
#         ("status", response.status_code, "yellow"),
#         ("duration", duration, "green"),
#         ("time", dt.timestamp, "magenta"),
#         ("ip", ip, "red"),
#         ("host", host, "red"),
#         ("params", args, "blue"),
#     ]

#     request_id = request.headers.get("X-Request-ID")
#     if request_id:
#         log_params.append(("request_id", request_id, "yellow"))

#     parts = []
#     for name, value, color in log_params:
#         part = colors.color("{}={}".format(name, value), fg=color)
#         parts.append(part)
#     line = " ".join(parts)

#     application.logger.info(line)

#     return response


if __name__ == "__main__":
    application.run()
