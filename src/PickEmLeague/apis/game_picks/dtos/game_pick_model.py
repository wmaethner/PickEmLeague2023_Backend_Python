"""Parsers and serializers for /auth API endpoints."""
from flask_restx import Model
from flask_restx.fields import Integer, String

from ...core.base_model import BaseModel

game_pick_data = Model(
    "GamePickData",
    {
        "user_id": Integer,
        "game_id": Integer,
        "pick": String,
        "amount": Integer,
    },
)
game_pick_model = BaseModel("GamePickModel", game_pick_data).model()
