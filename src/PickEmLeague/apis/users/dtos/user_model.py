"""Parsers and serializers for /auth API endpoints."""
from flask import Response
from flask_restx import Model
from flask_restx.fields import Boolean, Integer, String

from ...core.base_model import BaseModel

user_data = Model(
    "UserData",
    {
        "id": Integer,
        "first_name": String,
        "last_name": String,
        "email": String,
        "admin": Boolean,
    },
)
user_model = BaseModel("UserResult", user_data).model()
