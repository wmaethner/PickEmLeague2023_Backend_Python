from flask_restx import Model
from flask_restx.fields import Boolean, Integer, Nested, String

from ..core.base_schema import BaseModel
from ..users.user_schema import user_schema

summary_schema = Model(
    "SummarySchema",
    {"user": Nested(user_schema), "score": Integer, "correct_picks": Integer},
)

summaries_model = BaseModel("SummariesModel", summary_schema).list_model()
