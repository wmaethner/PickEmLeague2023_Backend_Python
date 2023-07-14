from datetime import datetime, timedelta, timezone
from typing import List, Optional

import jwt
from flask import current_app

from src.PickEmLeague import bcrypt, db
from src.PickEmLeague.util.result import Result


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    @property
    def password(self):
        raise Exception("write only field")

    @password.setter
    def password(self, password) -> bool:
        log_rounds = current_app.config.get("BCRYPT_LOG_ROUNDS")
        hash_bytes = bcrypt.generate_password_hash(password, log_rounds)
        self.password_hash = hash_bytes.decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def encode_access_token(self):
        now = datetime.now(timezone.utc)
        token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
        token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
        expire = now + timedelta(hours=token_age_h, minutes=token_age_m)
        if current_app.config["TESTING"]:
            expire = now + timedelta(seconds=5)
        payload = dict(exp=expire, iat=now, sub=self.id, admin=self.admin)
        key = current_app.config.get("SECRET_KEY")
        return jwt.encode(payload, key, algorithm="HS256")

    @staticmethod
    def decode_access_token(access_token):
        if isinstance(access_token, bytes):
            access_token = access_token.decode("ascii")
        if access_token.startswith("Bearer "):
            split = access_token.split("Bearer")
            access_token = split[1].strip()
        try:
            key = current_app.config.get("SECRET_KEY")
            payload = jwt.decode(access_token, key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            error = "Access token expired. Please log in again."
            return Result.Fail(error)
        except jwt.InvalidTokenError:
            error = "Invalid token. Please log in again."
            return Result.Fail(error)

        user_dict = dict(
            id=payload["sub"],
            admin=payload["admin"],
            token=access_token,
            expires_at=payload["exp"],
        )
        return Result.Ok(user_dict)

    @classmethod
    def find_by_email_or_username(cls, email_or_username) -> Optional["User"]:
        user = User.find_by_email(email_or_username)
        user = User.find_by_username(email_or_username) if not user else user
        return user

    @classmethod
    def find_by_email(cls, email) -> "User":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username) -> "User":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_all(cls) -> List["User"]:
        return cls.query.all()
