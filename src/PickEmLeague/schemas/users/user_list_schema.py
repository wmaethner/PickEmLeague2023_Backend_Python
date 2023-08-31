from ..core.base_schema import BaseModel
from .user_schema import user_schema

user_list_model = BaseModel("UserListModel", user_schema).list_model()
