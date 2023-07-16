from flask_restx import Namespace, Resource

from .business import login_user, register_user
from .dtos.parsers import auth_user_parser

auth_ns = Namespace(name="auth", validate=True)


@auth_ns.route("/register")
class RegisterUser(Resource):
    @auth_ns.expect(auth_user_parser)
    def post(self):
        user_dict = auth_user_parser.parse_args()
        return register_user(
            user_dict.get("email"), user_dict.get("username"), user_dict.get("password")
        )


@auth_ns.route("/login")
class LoginUser(Resource):
    @auth_ns.expect(auth_user_parser)
    def post(self):
        user_dict = auth_user_parser.parse_args()
        return login_user(user_dict.get("email"), user_dict.get("password"))
