from ..core.base_schema import BaseModel
from .game_pick_schema import game_pick_schema

game_pick_list_model = BaseModel("GamePickListModel", game_pick_schema).list_model()
