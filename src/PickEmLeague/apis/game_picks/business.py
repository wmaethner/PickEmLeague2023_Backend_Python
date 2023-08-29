from src.PickEmLeague.apis.core.base_model import BaseModel
from src.PickEmLeague.models.game_pick import GamePick
from src.PickEmLeague.models.user import User


def get_game_pick_list():
    games = GamePick.find_all()
    return map_game_picks(games)


def get_game_picks_by_week(week: int):
    return map_game_picks(GamePick.find_by_week(week))


def get_game_picks_by_user_and_week(user_id: int, week: int):
    user = User.find_by_id(user_id)
    return map_game_picks(GamePick.find_by_user_and_week(user, week))


def map_game_picks(game_picks: [GamePick]):
    return BaseModel.SuccessResult([gp.to_json() for gp in game_picks])
