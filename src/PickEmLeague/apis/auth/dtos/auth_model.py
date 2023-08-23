"""Parsers and serializers for /auth API endpoints."""
from flask import Response
from flask_restx import Model
from flask_restx.fields import String

from ...core.base_model import BaseModel

auth_data = Model("AuthData", {"token": String})
auth_model = BaseModel("AuthResult", auth_data).model()
