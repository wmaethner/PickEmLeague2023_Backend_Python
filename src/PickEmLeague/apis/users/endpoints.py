from flask import jsonify, request
from flask_restx import Resource

from src.PickEmLeague.decorators.auth import token_required
from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.users.user_list_schema import user_list_model
from src.PickEmLeague.schemas.users.user_schema import user_model, user_schema

from ..core.base_namespace import BaseNamespace
from .business import get_current_user, get_user_list

user_ns = BaseNamespace(name="users", validate=True)
user_ns.add_models([user_schema, user_model, user_list_model])


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


@user_ns.route("/<int:id>")
class UserById(Resource):
    @user_ns.marshal_with(user_model)
    def get(self, id):
        """Retrieve a list of users."""
        user_ns.logger.info("Getting user list")
        try:
            user = jsonify(User.find_by_id(id))
            print(user.data)
        except Exception as e:
            print(e)
        return get_user_list()


@user_ns.route("/clear-all")
class ClearUserList(Resource):
    def get(self):
        """Clear out all users."""
        return User.clear_all()
