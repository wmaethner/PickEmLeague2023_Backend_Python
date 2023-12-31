import logging

from flask import Blueprint
from flask_restx import Api

from src.PickEmLeague.apis.auth.endpoints import auth_ns
from src.PickEmLeague.apis.game_picks.endpoints import game_picks_ns
from src.PickEmLeague.apis.games.endpoints import game_ns
from src.PickEmLeague.apis.messages.endpoints import messages_ns
from src.PickEmLeague.apis.misc.endpoints import misc_ns
from src.PickEmLeague.apis.push_notifications.endpoints import push_notifications_ns
from src.PickEmLeague.apis.release_notes.endpoints import release_notes_ns
from src.PickEmLeague.apis.scheduler.endpoints import scheduler_ns
from src.PickEmLeague.apis.summaries.endpoints import summary_ns
from src.PickEmLeague.apis.teams.endpoints import team_ns
from src.PickEmLeague.apis.user_settings.endpoints import user_settings_ns
from src.PickEmLeague.apis.users.endpoints import user_ns

api_bp = Blueprint("api", __name__, url_prefix="/api")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    api_bp,
    version="1.0",
    title="Pick Em League Swagger",
    description="Welcome to the Swagger UI documentation site!",
    doc="/swagger",
    authorizations=authorizations,
)

api.add_namespace(user_ns, path="/users")
api.add_namespace(auth_ns, path="/auth")
api.add_namespace(team_ns, path="/teams")
api.add_namespace(game_ns, path="/games")
api.add_namespace(game_picks_ns, path="/game_picks")
api.add_namespace(misc_ns, path="/misc")
api.add_namespace(summary_ns, path="/summaries")
api.add_namespace(release_notes_ns, path="/release_notes")
api.add_namespace(messages_ns, path="/messages")
api.add_namespace(scheduler_ns, path="/scheduler")
api.add_namespace(push_notifications_ns, path="/push_notifications")
api.add_namespace(user_settings_ns, path="/user_settings")
