from flask_restx import Model
from flask_restx.fields import Integer, Nested

from ..core.base_schema import BaseModel
from ..games.game_schema import game_schema
from ..users.user_schema import user_schema

game_pick_schema = Model(
    "GamePickSchema",
    {
        "id": Integer,
        "user": Nested(user_schema),
        "game": Nested(game_schema),
        "pick": Integer,
        "amount": Integer,
    },
)

game_pick_model = BaseModel("GamePickModel", game_pick_schema).model()
