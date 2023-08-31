from flask_restx import Model
from flask_restx.fields import String

from ..core.base_schema import BaseModel

auth_schema = Model("AuthSchema", {"token": String})

auth_model = BaseModel("AuthModel", auth_schema).model()
