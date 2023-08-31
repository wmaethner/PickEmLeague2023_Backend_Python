from flask_restx import Model
from flask_restx.fields import Boolean, Integer, Nested, String

from ..core.base_schema import BaseModel
from ..users.user_schema import user_schema

week_summary_schema = Model(
    "WeekSummarySchema",
    {"user": Nested(user_schema), "score": Integer, "correct_picks": Integer},
)

week_summaries_model = BaseModel("WeekSummariesModel", week_summary_schema).list_model()
