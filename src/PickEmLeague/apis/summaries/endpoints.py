from flask_restx import Namespace, Resource

from src.PickEmLeague.schemas.summaries.summary_schema import (
    summaries_model,
    summary_schema,
)

from ..core.base_namespace import BaseNamespace
from .business import get_season_summaries, get_week_summaries

summary_ns = BaseNamespace(name="summaries", validate=True)
summary_ns.add_models([summary_schema, summaries_model])


@summary_ns.errorhandler
def error(error):
    print(error)
    return {"message": error}


@summary_ns.route("/week/<int:week>")
class WeekSummary(Resource):
    @summary_ns.marshal_with(summaries_model)
    def get(self, week):
        summaries = get_week_summaries(week)
        return summaries


@summary_ns.route("/season")
class SeasonSummary(Resource):
    @summary_ns.marshal_with(summaries_model)
    def get(self):
        summaries = get_season_summaries()
        return summaries
