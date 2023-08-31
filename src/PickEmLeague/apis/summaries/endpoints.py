from flask_restx import Namespace, Resource

from src.PickEmLeague.schemas.summaries.week_summary_schema import (
    week_summaries_model,
    week_summary_schema,
)

from ..core.base_namespace import BaseNamespace
from .business import get_week_summaries

summary_ns = BaseNamespace(name="summaries", validate=True)
summary_ns.add_models([week_summary_schema, week_summaries_model])


@summary_ns.errorhandler
def error(error):
    print(error)
    return {"message": error}


@summary_ns.route("/week/<int:week>")
class WeekSummary(Resource):
    @summary_ns.marshal_with(week_summaries_model)
    def get(self, week):
        try:
            summaries = get_week_summaries(week)
        except Exception as e:
            print(e)
        return summaries
