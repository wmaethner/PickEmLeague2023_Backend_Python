"""Parsers and serializers for /auth API endpoints."""
from flask_restx import Model
from flask_restx.fields import Boolean, String

auth_model = Model(
    "AuthResult",
    {"success": Boolean, "token": String},
)
