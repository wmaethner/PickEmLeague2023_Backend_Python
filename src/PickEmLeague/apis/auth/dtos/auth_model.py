"""Parsers and serializers for /auth API endpoints."""
from flask import Response
from flask_restx import Model
from flask_restx.fields import Boolean, Integer, String

auth_model = Model(
    "AuthResult",
    {"success": Boolean, "token": String, "message": String},
    # {
    #     "access_token": String,
    #     "expires_in": Integer,
    #     "message": String,
    #     "status": String,
    #     "token_type": String,
    # },
)
