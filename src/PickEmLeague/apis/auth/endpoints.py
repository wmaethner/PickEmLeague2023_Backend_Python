from flask import jsonify
from flask_restx import Namespace, Resource

from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.auth.auth_schema import auth_model, auth_schema

from ..core.base_namespace import BaseNamespace
from .business import login_user, register_user
from .parsers import auth_login_parser, auth_register_parser

auth_ns = BaseNamespace(name="auth", validate=True)
auth_ns.add_models([auth_schema, auth_model])


@auth_ns.route("/register")
class RegisterUser(Resource):
    @auth_ns.expect(auth_register_parser)
    @auth_ns.marshal_with(auth_model)
    def post(self):
        user_dict = auth_register_parser.parse_args()
        return register_user(
            user_dict.get("first_name"),
            user_dict.get("last_name"),
            user_dict.get("email"),
            user_dict.get("username"),
            user_dict.get("password"),
        )


@auth_ns.route("/login")
class LoginUser(Resource):
    @auth_ns.expect(auth_login_parser)
    @auth_ns.marshal_with(auth_model)
    def post(self):
        user_dict = auth_login_parser.parse_args()
        username = user_dict.get("username")
        password = user_dict.get("password")
        result = login_user(username, password)
        return result
