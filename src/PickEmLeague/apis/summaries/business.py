from src.PickEmLeague.models.game import Game
from src.PickEmLeague.models.game_pick import GamePick
from src.PickEmLeague.models.user import User


def get_week_summaries(week: int):
    users = User.find_all()
    summaries = []
    for user in users:
        summaries.append(week_summary_for_user(week, user))
    return summaries


def week_summary_for_user(week: int, user: User):
    games = Game.find_by_week(week)
    game_picks = GamePick.find_by_user_and_week(user, week)
    score, correct = 0, 0
    for g in games:
        gp = next((x for x in game_picks if x.game_id == g.id), None)
        if gp:
            if gp.pick == g.result:
                score += gp.amount
                correct += 1
        else:
            # Throw error?
            pass
    return {"user": user, "score": score, "correct_picks": correct}
