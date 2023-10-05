from flask_restx import Model
from flask_restx.fields import DateTime, Integer, Nested, String

from ..core.base_schema import BaseModel
from ..users.user_schema import user_schema

message_schema = Model(
    "MessageSchema",
    {"id": Integer, "text": String, "user": Nested(user_schema), "created_at": String},
)

message_model = BaseModel("MessageModel", message_schema).model()
message_list_model = BaseModel("MessageModel", message_schema).list_model()
