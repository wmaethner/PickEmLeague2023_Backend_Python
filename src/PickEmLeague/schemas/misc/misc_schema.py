from flask_restx import Model
from flask_restx.fields import Boolean

from ..core.base_schema import BaseModel

misc_schema = Model("MiscSchema", {"started": Boolean})

misc_model = BaseModel("MiscModel", misc_schema).model()
