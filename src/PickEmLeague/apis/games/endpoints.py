from flask import jsonify, request
from flask_restx import Namespace, Resource

from src.PickEmLeague import db
from src.PickEmLeague.models.game import Game
from src.PickEmLeague.models.team import Team
from src.PickEmLeague.schemas.games.game_list_schema import game_list_model
from src.PickEmLeague.schemas.games.game_schema import game_model, game_schema

from ..core.base_namespace import BaseNamespace
from .business import (
    get_game_by_id,
    get_game_list,
    get_games_by_week,
    load_games_from_csv,
    load_games_from_file,
    update_game,
)
from .parsers import game_list_upload_parser

game_ns = BaseNamespace(name="games", validate=True)
game_ns.add_models([game_schema, game_model, game_list_model])


@game_ns.errorhandler
def error_handler(error):
    print(error)
    return {"message": str(error)}, getattr(error, "code", 500)


@game_ns.route("/<int:id>")
class GameById(Resource):
    @game_ns.marshal_with(game_model)
    def get(self, id):
        return get_game_by_id(id)

    @game_ns.expect(game_schema)
    def put(self, id):
        update_game(id, request.get_json())


@game_ns.route("")
class GameList(Resource):
    @game_ns.marshal_with(game_list_model)
    def get(self):
        """Retrieve a list of games."""
        return get_game_list()

    @game_ns.expect(game_list_upload_parser)
    def post(self):
        args = game_list_upload_parser.parse_args()
        file = args["game-file"]
        # load_games_from_file(file)
        load_games_from_csv(file)
        return {}


@game_ns.route("/by_week/<int:week>")
@game_ns.param("week", "Week number")
class GamesByWeek(Resource):
    @game_ns.marshal_with(game_list_model)
    def get(self, week):
        return get_games_by_week(week)


@game_ns.route("/<week>/<abbr>")
@game_ns.param("week", "Week number")
@game_ns.param("abbr", "Team")
class GameByWeekAndTeam(Resource):
    @game_ns.marshal_with(game_model)
    def get(self, week, abbr):
        team = Team.find_by_abbreviation(abbr)
        game = Game.find_by_week_and_team(week, team)
        return game
