import os

from src.PickEmLeague import create_app

application = app = create_app(os.getenv("FLASK_ENV", "development"))


@app.route("/")
def index():
    return "The index page"


if __name__ == "__main__":
    application.run()
