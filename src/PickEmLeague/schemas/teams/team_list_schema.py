from ..core.base_schema import BaseModel
from .team_schema import team_schema

team_list_model = BaseModel("TeamListModel", team_schema).list_model()
