import os

from src.PickEmLeague import create_app

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.route("/")
def index():
    return f'The index page {os.getenv("FLASK_ENV", "development")}'


if __name__ == "__main__":
    app.run()
