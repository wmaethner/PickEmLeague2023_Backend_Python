"""Parsers and serializers for /auth API endpoints."""
from flask_restx import Model
from flask_restx.fields import Integer, String

from src.PickEmLeague.models.team import Team

game_pick_model = Model(
    "GamePick",
    {
        "user_id": Integer,
        "game_id": Integer,
        "pick": String,
        "amount": Integer,
    },
)
