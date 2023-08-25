"""Parsers and serializers for /auth API endpoints."""
from flask import Response
from flask_restx import Model
from flask_restx.fields import Boolean, String

from ...core.base_model import BaseModel

misc_data = Model("MiscData", {"started": Boolean})
misc_model = BaseModel("MiscResult", misc_data).model()
