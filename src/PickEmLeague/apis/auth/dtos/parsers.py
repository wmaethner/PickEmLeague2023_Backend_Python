from flask_restx.inputs import email
from flask_restx.reqparse import RequestParser

auth_user_parser = RequestParser(bundle_errors=True)
auth_user_parser.add_argument(
    name="email", type=email(), location="form", required=True, nullable=False
)
auth_user_parser.add_argument(
    name="username", type=str, location="form", required=True, nullable=False
)
auth_user_parser.add_argument(
    name="password", type=str, location="form", required=True, nullable=False
)
