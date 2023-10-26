from src.PickEmLeague import scheduler
from src.PickEmLeague.models.game import Game
from src.PickEmLeague.models.user import User
from src.PickEmLeague.services.push_notifications.send_notification import (
    send_notification,
)


def game_pick_notification(user_id: int, game_id: int):
    with scheduler.app.app_context():
        user = User.find_by_id(user_id)
        game = Game.find_by_id(game_id)

        message = f"Make pick for {game.away_team.name} @ {game.home_team.name}"
        send_notification(user, message, 1)
