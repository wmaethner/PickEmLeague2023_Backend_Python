from src.PickEmLeague import db
from src.PickEmLeague.models import User, UserSettings


def update_user_settings(user: User, token: str):
    settings = UserSettings.find_by_user(user)
    if not settings:
        settings = UserSettings(user=user)
        db.session.add(settings)
    settings.push_token = token
    db.session.commit()
