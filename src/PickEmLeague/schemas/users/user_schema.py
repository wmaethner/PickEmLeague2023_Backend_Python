from flask_restx import Model
from flask_restx.fields import Boolean, Integer, String

from ..core.base_schema import BaseModel

user_schema = Model(
    "UserSchema",
    {
        "id": Integer,
        "username": String,
        "first_name": String,
        "last_name": String,
        "email": String,
        "admin": Boolean,
    },
)

user_model = BaseModel("UserModel", user_schema).model()
