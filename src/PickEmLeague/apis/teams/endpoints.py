from http import HTTPStatus
from typing import List

from flask import request
from flask_restx import Namespace, Resource

from src.PickEmLeague import db
from src.PickEmLeague.models.team import Team as TeamObject

from .business import get_team_list
from .dtos.parsers import team_list_upload_parser
from .dtos.team_model import team_model

team_ns = Namespace(name="teams", validate=True)
team_ns.models[team_model.name] = team_model


@team_ns.route("")
class TeamList(Resource):
    @team_ns.response(HTTPStatus.OK, "Retrieved team list.", [team_model])
    @team_ns.marshal_list_with(team_model)
    def get(self):
        """Retrieve a list of users."""
        print("Get team list")
        return get_team_list()

    @team_ns.expect(team_list_upload_parser)
    def post(self):
        args = team_list_upload_parser.parse_args()
        file = args["team-file"]
        for line in [l.strip() for l in file.readlines()][1::]:
            parts = line.decode("utf-8").split(",")
            new_team = TeamObject(
                id=int(parts[0]),
                name=parts[1].split(" ")[-1],
                city=" ".join(parts[1].split(" ")[0:-1]),
                abbreviation=parts[2],
                conference=parts[3],
                division=parts[4],
            )
            db.session.add(new_team)
            db.session.commit()


@team_ns.route("/by_id/<id>")
@team_ns.param("id", "Team ID")
class TeamById(Resource):
    @team_ns.marshal_with(team_model)
    def get(self, id):
        return TeamObject.find_by_id(id)


@team_ns.route("/by_abbr/<abbr>")
@team_ns.param("abbr", "Team abbreviation")
class TeamByAbbr(Resource):
    @team_ns.marshal_with(team_model)
    def get(self, abbr):
        return TeamObject.find_by_abbreviation(abbr)
