from src.PickEmLeague.models.enums import GameResult
from src.PickEmLeague.models.game import Game
from src.PickEmLeague.models.game_pick import GamePick
from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def get_week_summaries(week: int):
    users = User.find_all()
    summaries = []
    for user in users:
        summaries.append(_week_summary_for_user(week, user))
    return BaseModel.SuccessResult(summaries)


def get_season_summaries():
    users = User.find_all()
    summaries = []
    for user in users:
        summaries.append(_season_summary_for_user(user))
    return BaseModel.SuccessResult(summaries)


def _season_summary_for_user(user: User):
    games = Game.find_all()
    game_picks = GamePick.find_by_user(user)
    score, correct = 0, 0
    for g in games:
        gp = [x for x in game_picks if x.game == g][0]
        if gp:
            if g.result == GameResult.NOT_PLAYED:
                continue
            if gp.pick == g.result:
                score += gp.amount if gp.amount else 0
                correct += 1
        else:
            # Throw error?
            pass
    return {"user": user, "score": score, "correct_picks": correct}


def _week_summary_for_user(week: int, user: User):
    games = Game.find_by_week(week)
    game_picks = GamePick.find_by_user_and_week(user, week)
    score, correct = 0, 0
    for g in games:
        gp = [x for x in game_picks if x.game == g][0]
        if gp:
            if g.result == GameResult.NOT_PLAYED:
                continue
            if gp.pick == g.result:
                score += gp.amount if gp.amount else 0
                correct += 1
        else:
            # Throw error?
            pass
    return {"user": user, "score": score, "correct_picks": correct}
