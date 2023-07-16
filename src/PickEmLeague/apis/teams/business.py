from src.PickEmLeague.models.team import Team


def get_team_list():
    users = Team.find_all()
    return users
