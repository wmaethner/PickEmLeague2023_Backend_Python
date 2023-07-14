"""Parsers and serializers for /auth API endpoints."""
from flask_restx import Model
from flask_restx.fields import Boolean, String

user_model = Model(
    "User",
    {
        "email": String,
        "admin": Boolean,
    },
)
