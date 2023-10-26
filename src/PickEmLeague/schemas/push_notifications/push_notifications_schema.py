from flask_restx import Model
from flask_restx.fields import DateTime, Integer, Nested, String

from ..core.base_schema import BaseModel
from ..users.user_schema import user_schema

udpate_token_schema = Model("UpdateTokenSchema", {"token": String})
send_notification_schema = Model("SendNotificationSchema", {"message": String})

udpate_token_model = BaseModel("UpdateTokenModel", udpate_token_schema).model()
send_notification_model = BaseModel(
    "SendNotificationModel", send_notification_schema
).model()
