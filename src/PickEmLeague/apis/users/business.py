from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def get_current_user(request):
    token = request.headers["Authorization"]
    if not token:
        return BaseModel.ErrorResult("no token supplied")
    result = User.decode_access_token(token.split(" ")[1])
    user = User.find_by_id(result.value["id"])
    if not user:
        return BaseModel.ErrorResult(f"no user found with id {result.value['id']}")
    return BaseModel.SuccessResult(user)


def get_user_list():
    users = User.find_all()
    return BaseModel.SuccessResult(users)
