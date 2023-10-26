from PickEmLeague.services.push_notifications.send_notification import send_notification
from src.PickEmLeague.models import UserSettings


def send_new_message_notifications():
    users = [x.user for x in UserSettings.find_all() if x.message_notification_enabled]
    for user in users:
        send_notification(user, "New message")
