from typing import List

from src.PickEmLeague import db
from src.PickEmLeague.models.enums import GameResult
from src.PickEmLeague.models.team import Team


class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_time = db.Column(db.DateTime)
    week = db.Column(db.Integer)
    result = db.Column(db.Enum(GameResult), default=GameResult.NOT_PLAYED)
    home_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    home_team = db.relationship("Team", lazy=True, foreign_keys=[home_team_id])
    away_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    away_team = db.relationship("Team", lazy=True, foreign_keys=[away_team_id])

    @classmethod
    def find_by_id(cls, id: int) -> "Game":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_week(cls, week: int) -> List["Game"]:
        return cls.query.filter_by(week=week).all()

    @classmethod
    def find_all(cls) -> List["Game"]:
        return cls.query.all()

    @classmethod
    def find_by_week_and_team(cls, week: int, team: Team) -> "Game":
        return cls.query.filter(
            (cls.week == week) & ((cls.home_team == team) | (cls.away_team == team))
        ).first()
