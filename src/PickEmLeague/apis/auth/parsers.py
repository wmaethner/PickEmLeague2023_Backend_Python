from flask_restx.inputs import email
from flask_restx.reqparse import RequestParser

auth_register_parser = RequestParser(bundle_errors=True)
auth_register_parser.add_argument(
    name="first_name", type=str, location="form", required=True, nullable=False
)
auth_register_parser.add_argument(
    name="last_name", type=str, location="form", required=True, nullable=False
)
auth_register_parser.add_argument(
    name="email", type=email(), location="form", required=True, nullable=False
)
auth_register_parser.add_argument(
    name="username", type=str, location="form", required=True, nullable=False
)
auth_register_parser.add_argument(
    name="password", type=str, location="form", required=True, nullable=False
)

auth_login_parser = RequestParser(bundle_errors=True)
auth_login_parser.add_argument(
    name="username", type=str, location="form", required=True, nullable=False
)
auth_login_parser.add_argument(
    name="password", type=str, location="form", required=True, nullable=False
)
