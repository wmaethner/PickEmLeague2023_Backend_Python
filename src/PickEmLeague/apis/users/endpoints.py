from flask import g, jsonify, request
from flask_restx import Resource, fields

from src.PickEmLeague.decorators.auth import login_required, token_required
from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.core.base_schema import BaseModel
from src.PickEmLeague.schemas.users.user_list_schema import user_list_model
from src.PickEmLeague.schemas.users.user_schema import user_model, user_schema

from ..core.base_namespace import BaseNamespace
from .business import get_user, get_user_list, update_user, update_user_password

user_ns = BaseNamespace(name="users", validate=True)
user_ns.add_models([user_schema, user_model, user_list_model])


@user_ns.route("/current")
class CurrentUser(Resource):
    @login_required
    @user_ns.doc(security="Bearer")
    @user_ns.marshal_with(user_model)
    def get(self):
        return BaseModel.SuccessResult(g.user)


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
        return get_user(id)

    @user_ns.expect(user_schema)
    def put(self, id):
        return update_user(id, request.get_json())


@user_ns.route("/password/<int:id>")
class UpdateUserPassword(Resource):
    @user_ns.expect(
        user_ns.model(
            "UserPassword",
            {
                "password": fields.String,
            },
        )
    )
    def put(self, id):
        return update_user_password(id, request.get_json()["password"])


@user_ns.route("/clear-all")
class ClearUserList(Resource):
    def get(self):
        """Clear out all users."""
        return User.clear_all()
