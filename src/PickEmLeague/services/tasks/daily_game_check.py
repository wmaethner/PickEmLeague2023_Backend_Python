from datetime import datetime, timedelta

from src.PickEmLeague import scheduler
from src.PickEmLeague.models.enums import GameResult
from src.PickEmLeague.models.game import Game
from src.PickEmLeague.models.game_pick import GamePick
from src.PickEmLeague.models.user import User
from src.PickEmLeague.services.tasks.game_pick_notification import game_pick_notification


@scheduler.task("cron", id="upcoming_game_check", hour="*/4")
def daily_game_check():
    start = datetime.utcnow()
    end = start + timedelta(hours=10)
    games = Game.find_in_range(start, end)
    for game in games:
        picks = GamePick.find_by_game(game)
        unpicked = [x for x in picks if x.pick == GameResult.NOT_PLAYED]
        for pick in unpicked:
            if not task_exists(pick.user, pick.game) and pick.user.id == 10:
                schedule_task(pick.user, pick.game)


def schedule_task(user: User, game: Game):
    scheduler.add_job(
        task_id(user, game),
        game_pick_notification,
        run_date=schedule_time(game),
        args=[user.id, game.id],
    )


def schedule_time(game: Game):
    return game._game_time - timedelta(hours=1)


def task_exists(user: User, game: Game):
    return not (scheduler.get_job(task_id(user, game)) == None)


def task_id(user: User, game: Game):
    return f"notification-user-{user.id}-game-{game.id}"
