import os

import requests
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError

from src.PickEmLeague.models.user import User
from src.PickEmLeague.models.user_settings import UserSettings


def send_notification(user: User, message: str):
    print(f"send notification: {user} - {message}")
    token = push_token(user)
    if not token:
        print(f"No token for {user.first_name} {user.last_name}")
        return
    try:
        response = PushClient().publish(PushMessage(to=token, body=message, badge="!"))
        response.validate_response()
    except Exception as e:
        print(f"Send notification error for {user.first_name} {user.last_name}: {e}")


def push_token(user: User):
    settings = UserSettings.find_by_user(user)
    if not settings:
        print(f"No settings for {user.first_name} {user.last_name}")
        return None

    return settings.push_token
