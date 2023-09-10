from flask_restx import Model
from flask_restx.fields import Boolean, Integer, Nested, String

from ..core.base_schema import BaseModel
from ..users.user_schema import user_schema

pick_status_schema = Model(
    "PickStatusSchema",
    {"user": Nested(user_schema), "status": Integer},
)

pick_statuses_model = BaseModel("PickStatusesModel", pick_status_schema).list_model()
