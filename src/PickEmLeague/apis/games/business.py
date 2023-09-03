from datetime import datetime, timezone

import pytz

from src.PickEmLeague import db
from src.PickEmLeague.models.game import Game
from src.PickEmLeague.models.team import Team
from src.PickEmLeague.schemas.core.base_schema import BaseModel
from src.PickEmLeague.util.models import update_model


def get_game_list():
    return BaseModel.SuccessResult(Game.find_all())


def get_games_by_week(week: int):
    return BaseModel.SuccessResult(Game.find_by_week(week))


def get_game_by_id(id: int):
    return BaseModel.SuccessResult(Game.find_by_id(id))


def update_game(id: int, game_data: any):
    game = Game.find_by_id(id)
    if game:
        update_model(game, game_data, ["result", "game_time"], db)
        return BaseModel.SuccessResult(Game.find_by_id(id))
    return BaseModel.ErrorResult(f"Game with id {id} not found")


def load_games_from_file(file):
    for line in [l.decode("utf-8").strip() for l in file.readlines()]:
        parts = line.split(",")
        team = Team.find_by_abbreviation(parts[0])

        for week in range(1, 19):
            # Check for bye
            if parts[week] == "BYE":
                continue

            # Check if team has game for week already
            if Game.find_by_week_and_team(week, team):
                continue

            team_is_home = parts[week][0] != "@"
            other = Team.find_by_abbreviation(
                parts[week] if team_is_home else parts[week][1:]
            )
            new_game = Game(
                week=week,
                home_team=team if team_is_home else other,
                away_team=other if team_is_home else team,
            )
            db.session.add(new_game)
            db.session.commit()


def load_games_from_csv(file):
    week = 0
    date = None
    away = Team()
    home = Team()
    tz = pytz.timezone("America/New_York")
    try:
        for line in [l.decode("utf-8").strip() for l in file.readlines()]:
            parts = line.split(",")

            # Parse date and time
            if parts[0]:
                if "WEEK" in parts[0]:
                    week = int(parts[0][:-1].split(" ")[1])
                else:
                    date = datetime.strptime(parts[0], "%A %B %d %Y")
            if parts[2]:
                date = (
                    datetime.strptime(date.strftime("%Y-%m-%d"), "%Y-%m-%d")
                    if "TBD" in parts[2]
                    else datetime.strptime(
                        f"{date.strftime('%Y-%m-%d')} {parts[2]}", "%Y-%m-%d %I:%M %p"
                    )
                )

            # Parse teams
            if parts[1]:
                teams = [x.strip().split(" ") for x in parts[1].split("@")]
                away = Team.find_by_name(teams[0][-1])
                home = Team.find_by_name(teams[1][-1])
                date_timezone = tz.localize(date)
                new_game = Game(
                    week=week,
                    home_team=home,
                    away_team=away,
                    game_time=date_timezone.astimezone(timezone.utc).isoformat(),
                )
                db.session.add(new_game)
        db.session.commit()
    except Exception as e:
        print(e)
