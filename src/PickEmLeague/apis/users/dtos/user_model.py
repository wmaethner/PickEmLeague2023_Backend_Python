"""Parsers and serializers for /auth API endpoints."""
from flask import Response
from flask_restx import Model
from flask_restx.fields import Boolean, Integer, List, Nested, String

from ...core.base_model import BaseModel

user_data = Model(
    "UserData",
    {
        "id": Integer,
        "username": String,
        "first_name": String,
        "last_name": String,
        "email": String,
        "admin": Boolean,
    },
)

user_model = BaseModel("UserModel", user_data).model()
user_list_model = BaseModel("UserListModel", user_data).list_model()
