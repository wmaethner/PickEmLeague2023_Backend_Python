from flask_restx import Namespace, Resource

from src.PickEmLeague import db
from src.PickEmLeague.models.game import Game
from src.PickEmLeague.models.team import Team

from .business import get_game_list
from .dtos.game_model import game_model
from .dtos.parsers import game_list_upload_parser

game_ns = Namespace(name="games", validate=True)
game_ns.models[game_model.name] = game_model


@game_ns.route("")
class GameList(Resource):
    # @game_ns.response(HTTPStatus.OK, "Retrieved team list.", team_model)
    @game_ns.marshal_list_with(game_model)
    def get(self):
        """Retrieve a list of games."""
        return get_game_list()

    @game_ns.expect(game_list_upload_parser)
    def post(self):
        args = game_list_upload_parser.parse_args()
        file = args["game-file"]

        for line in [l.decode("utf-8").strip() for l in file.readlines()]:
            parts = line.split(",")
            team = Team.find_by_abbreviation(parts[0])

            for week in range(1, 19):
                # Check for bye
                if parts[week] == "BYE":
                    continue

                # Check if team has game for week already
                if Game.find_by_week_and_team(week, team):
                    continue

                team_is_home = parts[week][0] != "@"
                other = Team.find_by_abbreviation(
                    parts[week] if team_is_home else parts[week][1:]
                )
                new_game = Game(
                    week=week,
                    home_team=team if team_is_home else other,
                    away_team=other if team_is_home else team,
                )
                db.session.add(new_game)
                db.session.commit()


@game_ns.route("/<week>")
@game_ns.param("week", "Week number")
class GamesByWeek(Resource):
    @game_ns.marshal_list_with(game_model)
    def get(self, week):
        return Game.find_by_week(week)


# @game_ns.route("/<week>/<abbr>")
# @game_ns.param("week", "Week number")
# @game_ns.param("abbr", "Team")
# class GameByWeekAndTeam(Resource):
#     # @game_ns.marshal_with(game_model)
#     def get(self, week, abbr):
#         team = Team.find_by_abbreviation(abbr)
#         game = Game.find_by_week_and_team(week, team)
#         print(game)
#         if game:
#             return True
#         else:
#             return False
