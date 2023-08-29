from http import HTTPStatus

from flask import jsonify
from flask_restx import abort

from src.PickEmLeague import db
from src.PickEmLeague.apis.core.base_model import BaseModel
from src.PickEmLeague.models.user import User


def get_current_user(request):
    token = request.headers["Authorization"]
    if not token:
        return BaseModel.ErrorResult("no token supplied")
    result = User.decode_access_token(token.split(" ")[1])
    user = User.find_by_id(result.value["id"])
    if not user:
        return BaseModel.ErrorResult(f"no user found with id {result.value['id']}")
    return BaseModel.SuccessResult(user.to_json())


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
    return BaseModel.SuccessResult([user.to_json() for user in users])
