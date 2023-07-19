from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

game_list_upload_parser = RequestParser()
game_list_upload_parser.add_argument(
    "game-file", location="files", type=FileStorage, required=True
)
