from src.PickEmLeague import db
from src.PickEmLeague.decorators.api_result import api_result
from src.PickEmLeague.models import User, UserSettings
from src.PickEmLeague.util.models import update_model


@api_result
def get_user_settings(user: User):
    return UserSettings.find_by_user(user)


def toggle_pick_notification(user: User):
    _toggle_value(user, "pick_notification_enabled")


def toggle_message_notification(user: User):
    _toggle_value(user, "message_notification_enabled")


def _toggle_value(user: User, property: str):
    settings = UserSettings.find_by_user(user)
    update_model(
        settings,
        {property: not bool(getattr(settings, property))},
        [property],
        db,
    )
