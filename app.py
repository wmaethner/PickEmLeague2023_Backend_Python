import os

from src.PickEmLeague import create_app

application = create_app(os.getenv("FLASK_ENV", "development"))


@application.route("/")
def index():
    return f'The index page {os.getenv("FLASK_ENV", "development")}'


if __name__ == "__main__":
    application.run()
