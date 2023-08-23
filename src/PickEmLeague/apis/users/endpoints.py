from http import HTTPStatus

from flask_restx import Namespace, Resource

from src.PickEmLeague.models.user import User

from .business import get_user_list
from .dtos.user_model import user_model

user_ns = Namespace(name="users", validate=True)
user_ns.models[user_model.name] = user_model


@user_ns.route("/")
class UserList(Resource):
    @user_ns.response(HTTPStatus.OK, "Retrieved user list.", user_model)
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """Retrieve a list of users."""
        return get_user_list()


@user_ns.route("/clear-all")
class ClearUserList(Resource):
    def get(self):
        """Clear out all users."""
        return User.clear_all()
