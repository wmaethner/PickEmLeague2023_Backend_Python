from flask_restx.reqparse import RequestParser

release_notes_parser = RequestParser(bundle_errors=True)
release_notes_parser.add_argument(
    name="title", type=str, location="form", required=True, nullable=False
)
release_notes_parser.add_argument(
    name="date", type=str, location="form", required=True, nullable=False
)

release_notes_entry_parser = RequestParser(bundle_errors=True)
release_notes_entry_parser.add_argument(
    name="entry", type=str, location="form", required=True, nullable=False
)
