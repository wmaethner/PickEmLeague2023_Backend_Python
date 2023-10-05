from flask_restx.reqparse import RequestParser

new_message_parser = RequestParser(bundle_errors=True)
new_message_parser.add_argument(
    name="text", type=str, location="form", required=True, nullable=False
)
