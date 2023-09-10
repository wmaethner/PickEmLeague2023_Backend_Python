from src.PickEmLeague import db
from src.PickEmLeague.models.user import User
from src.PickEmLeague.schemas.core.base_schema import BaseModel
from src.PickEmLeague.util.models import update_model


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


def get_user(id: int):
    user = User.find_by_id(id)
    return BaseModel.SuccessResult(user)


def update_user(id: int, user_data: any):
    user = User.find_by_id(id)
    if user:
        update_model(user, user_data, ["password"], db)
        return BaseModel.SuccessResult(User.find_by_id(id))
    return BaseModel.ErrorResult(f"User with id {id} not found")


def update_user_password(id: int, password: str):
    user = User.find_by_id(id)
    user.password = password
    db.session.commit()
