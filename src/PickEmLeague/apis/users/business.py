from src.PickEmLeague import db
from src.PickEmLeague.decorators.api_result import api_result
from src.PickEmLeague.models.user import User
from src.PickEmLeague.util.models import update_model


@api_result
def get_user_list():
    return User.find_all()


@api_result
def get_user(id: int):
    return User.find_by_id(id)


@api_result
def update_user(id: int, user_data: any):
    user = User.find_by_id(id)
    update_model(user, user_data, ["password"], db)
    return User.find_by_id(id)


def update_user_password(id: int, password: str):
    user = User.find_by_id(id)
    user.password = password
    db.session.commit()
