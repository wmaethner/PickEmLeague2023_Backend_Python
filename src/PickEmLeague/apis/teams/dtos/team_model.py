"""Parsers and serializers for /auth API endpoints."""
from flask_restx import Model
from flask_restx.fields import String

team_model = Model(
    "Team",
    {
        "name": String,
        "city": String,
        "abbreviation": String,
        "conference": String,
        "division": String,
    },
)
