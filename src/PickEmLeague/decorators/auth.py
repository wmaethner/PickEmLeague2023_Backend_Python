from functools import wraps

from flask import g, request

from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not request.headers["Authorization"]:
            return BaseModel.ErrorResult("No authorization provided")
        user = User.authorized_user(request.headers["Authorization"])
        g.user = user
        return f(*args, **kwargs)

    return wrap
