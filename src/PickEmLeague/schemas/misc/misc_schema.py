from flask_restx import Model
from flask_restx.fields import Boolean, Integer, Nested

from ..core.base_schema import BaseModel

version_schema = Model(
    "VersionSchema", {"ios": Integer, "android": Integer, "server": Integer}
)
misc_schema = Model(
    "MiscSchema", {"started": Boolean, "versions": Nested(version_schema)}
)

misc_model = BaseModel("MiscModel", misc_schema).model()
