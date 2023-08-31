from ..core.base_schema import BaseModel
from .game_schema import game_schema

game_list_model = BaseModel("GameListModel", game_schema).list_model()
