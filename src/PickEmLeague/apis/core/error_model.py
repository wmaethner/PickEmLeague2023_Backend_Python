"""Parsers and serializers for /auth API endpoints."""
from flask import Response
from flask_restx import Model
from flask_restx.fields import Boolean, Integer, String

error_model = Model(
    "ErrorModel",
    {"success": Boolean, "error": String}
    # {
    #     "access_token": String,
    #     "expires_in": Integer,
    #     "message": String,
    #     "status": String,
    #     "token_type": String,
    # },
)
