from flask_restx.reqparse import RequestParser

update_token_parser = RequestParser(bundle_errors=True)
update_token_parser.add_argument(
    name="token", type=str, location="form", required=True, nullable=False
)
