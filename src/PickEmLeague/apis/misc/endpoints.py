from http import HTTPStatus

from flask import current_app, request
from flask_restx import Namespace, Resource

from PickEmLeague.apis.core.base_model import BaseModel
from src.PickEmLeague import db
from src.PickEmLeague.models.team import Team as TeamObject

from .dtos.misc_model import misc_data, misc_model

misc_ns = Namespace(name="misc", validate=True)
misc_ns.models[misc_data.name] = misc_data
misc_ns.models[misc_model.name] = misc_model


@misc_ns.route("")
class MiscInfo(Resource):
    @misc_ns.marshal_with(misc_model)
    def get(self):
        return BaseModel.SuccessResult({"started": False})
