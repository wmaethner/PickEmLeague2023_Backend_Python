from http import HTTPStatus

from flask import current_app, jsonify
from flask_restx import abort

from src.PickEmLeague import db
from src.PickEmLeague.models.user import User


def register_user(email: str, username: str, password: str):
    if User.find_by_email(email):
        abort(HTTPStatus.CONFLICT, f"{email} is already registered", status="fail")
    if User.find_by_username(username):
        abort(HTTPStatus.CONFLICT, f"{username} is already registered", status="fail")
    new_user = User(email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    access_token = new_user.encode_access_token()
    return _create_auth_successful_response(
        token=access_token,
        status_code=HTTPStatus.CREATED,
        message="successfully registered",
    )


def login_user(email_or_username, password):
    user = User.find_by_email_or_username(email_or_username)
    if not user or not user.check_password(password):
        abort(
            HTTPStatus.UNAUTHORIZED,
            "email/username or password does not match",
            status="fail",
        )
    access_token = user.encode_access_token()
    return _create_auth_successful_response(
        token=access_token,
        status_code=HTTPStatus.OK,
        message="successfully logged in",
    )


def _create_auth_successful_response(token, status_code, message):
    response = jsonify(
        status="success",
        message=message,
        access_token=token,
        token_type="bearer",
        expires_in=_get_token_expire_time(),
    )
    response.status_code = status_code
    return response


def _get_token_expire_time():
    token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
    token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
    expires_in_seconds = token_age_h * 3600 + token_age_m * 60
    return expires_in_seconds if not current_app.config["TESTING"] else 5
