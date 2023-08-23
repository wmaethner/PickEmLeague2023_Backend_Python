from flask import current_app

from src.PickEmLeague import db
from src.PickEmLeague.apis.core.base_model import BaseModel
from src.PickEmLeague.models.user import User


def register_user(first: str, last: str, email: str, username: str, password: str):
    if User.find_by_email(email):
        return BaseModel.ErrorResult(f"{email} is already registered")
    if User.find_by_username(username):
        return BaseModel.ErrorResult(f"{username} is already registered")
    new_user = User(
        first_name=first,
        last_name=last,
        email=email,
        username=username,
        password=password,
    )
    db.session.add(new_user)
    db.session.commit()
    access_token = new_user.encode_access_token()
    return BaseModel.SuccessResult({"token": access_token}, "successfully registered")


def login_user(email_or_username, password):
    user = User.find_by_email_or_username(email_or_username)
    if not user or not user.check_password(password):
        return BaseModel.ErrorResult("email/username or password does not match")
    access_token = user.encode_access_token()
    return BaseModel.SuccessResult({"token": access_token}, "successfully logged in")


def _get_token_expire_time():
    token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
    token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
    expires_in_seconds = token_age_h * 3600 + token_age_m * 60
    return expires_in_seconds if not current_app.config["TESTING"] else 5
