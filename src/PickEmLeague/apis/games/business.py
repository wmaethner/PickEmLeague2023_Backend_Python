from src.PickEmLeague.models.game import Game
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def get_game_list():
    return BaseModel.SuccessResult(Game.find_all())


def get_games_by_week(week: int):
    return BaseModel.SuccessResult(Game.find_by_week(week))
