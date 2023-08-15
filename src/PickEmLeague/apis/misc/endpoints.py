from http import HTTPStatus

from flask import current_app, request
from flask_restx import Namespace, Resource

from src.PickEmLeague import db
from src.PickEmLeague.models.team import Team as TeamObject

misc_ns = Namespace(name="misc", validate=True)


@misc_ns.route("")
class MiscInfo(Resource):
    def get(self):
        return {"DB_ADDRESS": current_app.config["SQLALCHEMY_DATABASE_URI"]}
