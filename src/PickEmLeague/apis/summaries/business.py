from timeit import default_timer as timer

from src.PickEmLeague import db
from src.PickEmLeague.models.enums import GameResult
from src.PickEmLeague.models.game import Game
from src.PickEmLeague.models.game_pick import GamePick
from src.PickEmLeague.models.season_stats import SeasonStats
from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def get_week_summaries(week: int):
    users = User.find_all()
    games = Game.find_by_week(week)
    summaries = []
    for user in users:
        summaries.append(_week_summary_for_user(week, user, games))
    summaries.sort(key=lambda x: x["score"], reverse=True)
    return BaseModel.SuccessResult(summaries)


def get_week_pick_statuses(week: int):
    users = User.find_all()
    pick_statuses = []
    for user in users:
        pick_statuses.append(_week_pick_status_for_user(week, user))
    return BaseModel.SuccessResult(pick_statuses)


def get_season_summaries():
    # start = timer()
    users = User.find_all()
    summaries = []
    for user in users:
        summaries.append(_season_summary_for_user(user))
    summaries.sort(key=lambda x: x["score"], reverse=True)
    return BaseModel.SuccessResult(summaries)


def refresh_season_summaries():
    for user in User.find_all():
        season_stats = SeasonStats.find_by_user(user)
        _refresh_season_score(user, season_stats)


def _season_summary_for_user(user: User):
    season_stats = SeasonStats.find_by_user(user)
    if season_stats.score is None:
        _refresh_season_score(user, season_stats)
        # game_picks = GamePick.find_by_user(user)
        # games = Game.find_all()
        # score, correct = 0, 0
        # for g in games:
        #     gp = [x for x in game_picks if x.game == g][0]
        #     if gp:
        #         if g.result == GameResult.NOT_PLAYED:
        #             continue
        #         if gp.pick == g.result:
        #             score += gp.amount if gp.amount else 0
        #             correct += 1
        #     else:
        #         # Throw error?
        #         pass
        # season_stats.score = score
        # season_stats.correct_picks = correct
        # db.session.commit()
    return {
        "user": user,
        "score": season_stats.score,
        "correct_picks": season_stats.correct_picks,
    }


def _week_summary_for_user(week: int, user: User, games: [Game]):
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


def _week_pick_status_for_user(week: int, user: User):
    game_picks = GamePick.find_by_user_and_week(user, week)
    status = 0
    picks_made = [x != 1 for x in [gp.pick for gp in game_picks]]
    if all(picks_made):
        status = 2
    elif any(picks_made):
        status = 1
    return {"user": user, "status": status}


def _refresh_season_score(user: User, season_stats: SeasonStats):
    game_picks = GamePick.find_by_user(user)
    games = Game.find_all()
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
    season_stats.score = score
    season_stats.correct_picks = correct
    db.session.commit()
