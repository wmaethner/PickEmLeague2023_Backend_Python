from http import HTTPStatus

from flask import jsonify
from flask_restx import abort

from src.PickEmLeague import db
from src.PickEmLeague.models.user import User


def create_user(user_dict):
    email = user_dict["email"]
    if User.find_by_email(email):
        error = f"User email: {email} already exists, must be unique."
        abort(HTTPStatus.CONFLICT, error, status="fail")
    user = User(**user_dict)
    db.session.add(user)
    db.session.commit()
    response = jsonify(status="success", message=f"New user added: {email}.")
    response.status_code = HTTPStatus.CREATED
    # response.headers["Location"] = url_for("api.user", email=email)
    return response


def get_user_list():
    users = User.find_all()
    return users
