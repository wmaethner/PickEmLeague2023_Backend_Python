from flask import Blueprint
from flask_restx import Api

from src.PickEmLeague.apis.auth.endpoints import auth_ns
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
