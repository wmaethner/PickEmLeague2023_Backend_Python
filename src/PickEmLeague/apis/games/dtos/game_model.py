"""Parsers and serializers for /auth API endpoints."""
from flask_restx import Model
from flask_restx.fields import Integer, String

from src.PickEmLeague.models.enums import GameResult
from src.PickEmLeague.models.team import Team

game_model = Model(
    "Game",
    {
        "week": Integer,
        "result": String(enum=[e.value for e in GameResult]),
        "home_team_id": Integer,
        "away_team_id": Integer,
    },
)
