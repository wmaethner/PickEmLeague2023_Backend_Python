from flask import g, request
from flask_restx import Resource

from src.PickEmLeague.decorators.auth import login_required
from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.push_notifications import (
    send_notification_model,
    send_notification_schema,
    udpate_token_model,
    udpate_token_schema,
)
from src.PickEmLeague.services.push_notifications.send_notification import (
    send_notification,
)

from ..core.base_namespace import BaseNamespace
from .business import update_user_settings

push_notifications_ns = BaseNamespace(name="push_notifications", validate=True)
push_notifications_ns.add_models(
    [
        send_notification_model,
        send_notification_schema,
        udpate_token_model,
        udpate_token_schema,
    ]
)


@push_notifications_ns.route("/")
class Notifications(Resource):
    @login_required
    @push_notifications_ns.doc(security="Bearer")
    @push_notifications_ns.expect(udpate_token_model)
    def put(self):
        update_user_settings(g.user, request.get_json()["token"])

    @push_notifications_ns.expect(send_notification_model)
    def post(self):
        json = request.get_json()
        send_notification(User.find_by_id(10), json["message"])
