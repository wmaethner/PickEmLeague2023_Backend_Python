from flask_restx import Model
from flask_restx.fields import DateTime, Integer, Nested, String

from ..core.base_schema import BaseModel
from ..users.user_schema import user_schema

message_schema = Model(
    "MessageSchema",
    {"id": Integer, "text": String, "user": Nested(user_schema), "created_at": String},
)
last_message_read_schema = Model("LastMessageReadSchema", {"readable_id": Integer})

message_model = BaseModel("MessageModel", message_schema).model()
message_list_model = BaseModel("MessageModel", message_schema).list_model()
last_message_read_model = BaseModel(
    "LastMessageReadModel", last_message_read_schema
).model()
