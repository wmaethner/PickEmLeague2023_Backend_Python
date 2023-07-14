import pytest

from src.PickEmLeague import create_app
from src.PickEmLeague import db as database
from src.PickEmLeague.models.user import User


@pytest.fixture()
def app():
    app = create_app("testing")
    return app


@pytest.fixture
def db(app, client, request):
    database.drop_all()
    database.create_all()
    database.session.commit()

    def fin():
        database.session.remove()

    request.addfinalizer(fin)
    return database


@pytest.fixture
def user(db):
    # user = User(email=EMAIL, password=PASSWORD)
    user = User(email="test@test.com", password="PASSWORD")
    db.session.add(user)
    db.session.commit()
    return user


# @pytest.fixture()
# def client(app):
#     return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()
