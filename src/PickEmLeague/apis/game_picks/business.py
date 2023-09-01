from src.PickEmLeague.models.game_pick import GamePick
from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def get_game_pick_list():
    games = GamePick.find_all()
    return BaseModel.SuccessResult(games)


def get_game_picks_by_week(week: int):
    return BaseModel.SuccessResult(GamePick.find_by_week(week))


def get_game_picks_by_user_and_week(user_id: int, week: int):
    user = User.find_by_id(user_id)
    return BaseModel.SuccessResult(GamePick.find_by_user_and_week(user, week))
