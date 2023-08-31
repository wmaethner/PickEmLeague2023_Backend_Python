from http import HTTPStatus

from flask_restx import Namespace, Resource

from src.PickEmLeague import db
from src.PickEmLeague.schemas.game_picks.game_pick_list_schema import (
    game_pick_list_model,
)
from src.PickEmLeague.schemas.game_picks.game_pick_schema import (
    game_pick_model,
    game_pick_schema,
)

from ..core.base_namespace import BaseNamespace
from .business import (
    get_game_pick_list,
    get_game_picks_by_user_and_week,
    get_game_picks_by_week,
)

game_picks_ns = BaseNamespace(name="game_picks", validate=True)
game_picks_ns.add_models([game_pick_schema, game_pick_model, game_pick_list_model])


@game_picks_ns.route("")
class GamePickList(Resource):
    @game_picks_ns.response(HTTPStatus.OK, "Retrieved team list.", game_pick_model)
    @game_picks_ns.marshal_list_with(game_pick_model)
    def get(self):
        """Retrieve a list of game picks."""
        return get_game_pick_list()


@game_picks_ns.route("/<week>")
@game_picks_ns.param("week", "Week number")
class GamePicksByWeek(Resource):
    @game_picks_ns.marshal_list_with(game_pick_model)
    def get(self, week):
        return get_game_picks_by_week(week)


@game_picks_ns.route("/<week>/<user_id>")
@game_picks_ns.param("week", "Week number")
@game_picks_ns.param("user_id", "User ID")
class GamePicksByUserAndWeek(Resource):
    @game_picks_ns.marshal_list_with(game_pick_model)
    def get(self, week, user_id):
        return get_game_picks_by_user_and_week(user_id, week)
