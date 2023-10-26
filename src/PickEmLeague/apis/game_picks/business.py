from src.PickEmLeague import db
from src.PickEmLeague.decorators.api_result import api_result
from src.PickEmLeague.models.game_pick import GamePick
from src.PickEmLeague.models.user import User
from src.PickEmLeague.util.models import update_model


@api_result
def get_game_pick_by_id(id: int):
    return GamePick.find_by_id(id)


@api_result
def get_game_pick_list():
    return GamePick.find_all()


@api_result
def get_game_picks_by_week(week: int):
    return GamePick.find_by_week(week)


@api_result
def get_game_picks_by_user_and_week(user_id: int, week: int):
    user = User.find_by_id(user_id)
    return GamePick.find_by_user_and_week(user, week)


@api_result
def update_game_picks_by_user_and_week(user_id: int, week: int, game_pick_data: any):
    user = User.find_by_id(user_id)
    game_picks = GamePick.find_by_user_and_week(user, week)
    for index, pick_data in enumerate(game_pick_data):
        game_pick = GamePick.find_by_id(pick_data["id"])
        game_pick.amount = len(game_picks) - index
    db.session.commit()
    return GamePick.find_by_user_and_week(user, week)


# TODO: Remove pick notifications for this game (if they exist)
@api_result
def update_game_pick(id: int, game_pick_data: any):
    game_pick = GamePick.find_by_id(id)
    if game_pick:
        update_model(game_pick, game_pick_data, ["pick"], db)
        return GamePick.find_by_id(id)
