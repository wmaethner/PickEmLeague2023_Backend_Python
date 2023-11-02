import os
from http import HTTPStatus

from flask import current_app, request
from flask_restx import Namespace, Resource

from src.PickEmLeague import db
from src.PickEmLeague.schemas.core.base_schema import BaseModel
from src.PickEmLeague.schemas.misc.misc_schema import (
    misc_model,
    misc_schema,
    version_schema,
)
from src.PickEmLeague.util.paths import get_project_root

from ..core.base_namespace import BaseNamespace

misc_ns = BaseNamespace(name="misc", validate=True)
misc_ns.add_models([misc_schema, version_schema, misc_model])


@misc_ns.route("")
class MiscInfo(Resource):
    @misc_ns.marshal_with(misc_model)
    def get(self):
        file = open(f"{get_project_root()}/docs/server_version.txt")
        server_version = int(file.read())
        file.close()

        return BaseModel.SuccessResult(
            {
                "started": True,
                "current_week": 9,
                "versions": {"ios": 13, "android": 9, "server": server_version},
            }
        )
