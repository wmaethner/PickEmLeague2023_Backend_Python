from flask_restx import Model
from flask_restx.fields import Integer, List

from ..core.base_schema import BaseModel

read_ids_schema = Model("ReadIds", {"ids": List(Integer)})

read_ids_model = BaseModel("ReadIdsModel", read_ids_schema).model()
