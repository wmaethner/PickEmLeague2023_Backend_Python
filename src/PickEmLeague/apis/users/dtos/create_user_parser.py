from flask_restx.inputs import email
from flask_restx.reqparse import RequestParser

create_user_reqparser = RequestParser(bundle_errors=True)
create_user_reqparser.add_argument(
    name="email", type=email(), location="form", required=True, nullable=False
)

create_user_reqparser.add_argument(
    "admin",
    type=bool,
    location="form",
    required=True,
    nullable=False,
)
