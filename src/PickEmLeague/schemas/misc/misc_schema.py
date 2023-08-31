from flask_restx import Model
from flask_restx.fields import String

from ..core.base_schema import BaseModel

misc_schema = Model("MiscSchema", {"token": String})

misc_model = BaseModel("MiscModel", misc_schema).model()
