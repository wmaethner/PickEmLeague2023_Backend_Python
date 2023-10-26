from functools import wraps

from src.PickEmLeague.schemas.core.base_schema import BaseModel


def api_result(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            value = f(*args, **kwargs)
            return BaseModel.SuccessResult(value)
        except Exception as e:
            print(e)
            return BaseModel.ErrorResult(message=e)

    return wrap
