import logging

from flask import Blueprint
from flask_restx import Api

from src.PickEmLeague.apis.auth.endpoints import auth_ns
from src.PickEmLeague.apis.game_picks.endpoints import game_picks_ns
from src.PickEmLeague.apis.games.endpoints import game_ns
from src.PickEmLeague.apis.misc.endpoints import misc_ns
from src.PickEmLeague.apis.teams.endpoints import team_ns
from src.PickEmLeague.apis.users.endpoints import user_ns

api_bp = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    api_bp,
    version="1.0",
    title="Pick Em League Swagger",
    description="Welcome to the Swagger UI documentation site!",
    doc="/swagger",
    # authorizations=authorizations,
)

api.add_namespace(user_ns, path="/users")
api.add_namespace(auth_ns, path="/auth")
api.add_namespace(team_ns, path="/teams")
api.add_namespace(game_ns, path="/games")
api.add_namespace(game_picks_ns, path="/game_picks")
api.add_namespace(misc_ns, path="/misc")
