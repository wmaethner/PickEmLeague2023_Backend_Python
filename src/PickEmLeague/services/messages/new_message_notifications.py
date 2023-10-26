from src.PickEmLeague.models import UserSettings
from src.PickEmLeague.models.message import Message
from src.PickEmLeague.models.read import Read, Readables
from src.PickEmLeague.services.push_notifications.send_notification import (
    send_notification,
)


def send_new_message_notifications():
    users = [x.user for x in UserSettings.find_all() if x.message_notification_enabled]
    for user in users:
        send_notification(user, "New message", _get_unread_message_count(user))


def _get_unread_message_count(user):
    reads = Read.find_by_user_and_type(user.id, Readables.MESSAGES)
    messages = Message.find_after(reads[0].id if reads else 0)
    return len(messages)
