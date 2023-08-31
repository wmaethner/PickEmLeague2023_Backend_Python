from flask_restx import Model
from flask_restx.fields import DateTime, Integer, Nested, String

from ..core.base_schema import BaseModel
from ..teams.team_schema import team_schema

game_schema = Model(
    "GameSchema",
    {
        "id": Integer,
        "game_time": String,
        "week": Integer,
        "result": Integer,
        "home_team": Nested(team_schema),
        "away_team": Nested(team_schema),
    },
)

game_model = BaseModel("GameModel", game_schema).model()
