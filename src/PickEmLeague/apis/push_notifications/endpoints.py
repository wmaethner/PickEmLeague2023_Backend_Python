from flask import g, request
from flask_restx import Resource, fields

from src.PickEmLeague import db
from src.PickEmLeague.decorators.auth import login_required
from src.PickEmLeague.models.user import User
from src.PickEmLeague.models.user_settings import UserSettings

from ..core.base_namespace import BaseNamespace
from .business import send_push_message

push_notifications_ns = BaseNamespace(name="push_notifications", validate=True)


@push_notifications_ns.route("/")
class Notifications(Resource):
    @login_required
    @push_notifications_ns.doc(security="Bearer")
    @push_notifications_ns.expect(
        push_notifications_ns.model(
            "PushNotificationToken",
            {"token": fields.String},
        )
    )
    def put(self):
        user = g.user
        settings = UserSettings.find_by_user(user)
        if not settings:
            settings = UserSettings(user=user)
            db.session.add(settings)
        settings.push_token = request.get_json()["token"]
        db.session.commit()

    @push_notifications_ns.expect(
        push_notifications_ns.model(
            "PushNotification",
            {"userId": fields.Integer, "message": fields.String},
        )
    )
    def post(self):
        json = request.get_json()
        user = User.find_by_id()
        settings = UserSettings.find_by_user(user)
        send_push_message(settings.push_token, json["message"])
