from flask import jsonify
from flask_restx import Namespace, Resource

from src.PickEmLeague.models.user import User

from .business import login_user, register_user
from .dtos.auth_model import auth_data, auth_model
from .dtos.parsers import auth_login_parser, auth_register_parser

auth_ns = Namespace(name="auth", validate=True)
auth_ns.models[auth_data.name] = auth_data
auth_ns.models[auth_model.name] = auth_model


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
        print(f"Login for {username}")
        result = login_user(username, password)
        print(f"Result: {result}")
        return result
