from src.PickEmLeague.models.team import Team
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def get_team_list():
    teams = Team.find_all()
    return BaseModel.SuccessResult(teams)
