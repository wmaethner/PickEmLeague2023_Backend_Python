from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

team_list_upload_parser = RequestParser()
team_list_upload_parser.add_argument(
    "team-file", location="files", type=FileStorage, required=True
)
