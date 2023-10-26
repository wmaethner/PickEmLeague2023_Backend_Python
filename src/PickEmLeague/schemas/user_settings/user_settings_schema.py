from flask_restx import Model
from flask_restx.fields import Boolean, Integer

from ..core.base_schema import BaseModel

user_settings_schema = Model(
    "UserSettingsSchema",
    {
        "id": Integer,
        "pick_notification_enabled": Boolean,
        "message_notification_enabled": Boolean,
    },
)

user_settings_model = BaseModel("UserSettingsModel", user_settings_schema).model()
