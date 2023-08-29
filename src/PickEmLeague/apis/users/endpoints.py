from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource

from src.PickEmLeague.decorators.auth import token_required
from src.PickEmLeague.models.user import User

from .business import get_current_user, get_user_list
from .dtos.user_model import user_data, user_list_model, user_model

user_ns = Namespace(name="users", validate=True)
user_ns.models[user_data.name] = user_data
user_ns.models[user_model.name] = user_model
user_ns.models[user_list_model.name] = user_list_model


@user_ns.route("/current")
class CurrentUser(Resource):
    @token_required
    @user_ns.doc(security="Bearer")
    @user_ns.marshal_with(user_model)
    def get(self):
        return get_current_user(request)


@user_ns.route("/")
class UserList(Resource):
    @user_ns.marshal_with(user_list_model)
    def get(self):
        """Retrieve a list of users."""
        user_ns.logger.info("Getting user list")
        return get_user_list()


@user_ns.route("/clear-all")
class ClearUserList(Resource):
    def get(self):
        """Clear out all users."""
        return User.clear_all()
