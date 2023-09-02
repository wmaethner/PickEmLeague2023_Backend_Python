from src.PickEmLeague import db
from src.PickEmLeague.models.game import Game
from src.PickEmLeague.schemas.core.base_schema import BaseModel
from src.PickEmLeague.util.models import update_model


def get_game_list():
    return BaseModel.SuccessResult(Game.find_all())


def get_games_by_week(week: int):
    return BaseModel.SuccessResult(Game.find_by_week(week))


def get_game_by_id(id: int):
    return BaseModel.SuccessResult(Game.find_by_id(id))


def update_game(id: int, game_data: any):
    game = Game.find_by_id(id)
    if game:
        update_model(game, game_data, ["result", "game_time"], db)
        return BaseModel.SuccessResult(Game.find_by_id(id))
    return BaseModel.ErrorResult(f"Game with id {id} not found")
