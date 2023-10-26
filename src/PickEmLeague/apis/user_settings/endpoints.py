from flask import g
from flask_restx import Resource

from src.PickEmLeague.decorators.auth import login_required
from src.PickEmLeague.schemas.user_settings import (
    user_settings_model,
    user_settings_schema,
)

from ..core.base_namespace import BaseNamespace
from .business import (
    get_user_settings,
    toggle_message_notification,
    toggle_pick_notification,
)

user_settings_ns = BaseNamespace(name="user_settings", validate=True)
user_settings_ns.add_models([user_settings_schema, user_settings_model])


@user_settings_ns.route("/")
class Settings(Resource):
    @login_required
    @user_settings_ns.doc(security="Bearer")
    @user_settings_ns.marshal_with(user_settings_model)
    def get(self):
        return get_user_settings(g.user)


@user_settings_ns.route("/pick_notification")
class TogglePickNotification(Resource):
    @login_required
    @user_settings_ns.doc(security="Bearer")
    def put(self):
        toggle_pick_notification(g.user)


@user_settings_ns.route("/message_notification")
class ToggleMessageNotification(Resource):
    @login_required
    @user_settings_ns.doc(security="Bearer")
    def put(self):
        toggle_message_notification(g.user)
