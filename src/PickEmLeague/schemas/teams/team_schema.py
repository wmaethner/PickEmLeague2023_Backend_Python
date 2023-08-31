from flask_restx import Model
from flask_restx.fields import Boolean, Integer, String

from ..core.base_schema import BaseModel

team_schema = Model(
    "TeamSchema", {"id": Integer, "name": String, "city": String, "abbreviation": String}
)

team_model = BaseModel("team_model", team_schema).model()
