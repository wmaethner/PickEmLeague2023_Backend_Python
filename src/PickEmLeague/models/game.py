from dataclasses import dataclass
from datetime import datetime
from typing import List

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db
from src.PickEmLeague.models.enums import GameResult
from src.PickEmLeague.models.team import Team


@dataclass
class Game(db.Model):
    __tablename__ = "games"
    id: int
    week: int
    result: int
    home_team: Mapped[Team]
    away_team: Mapped[Team]
    game_time: Mapped[datetime]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    week = db.Column(db.Integer)
    result = db.Column(db.Enum(GameResult), default=GameResult.NOT_PLAYED)
    home_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    home_team = db.relationship("Team", lazy=True, foreign_keys=[home_team_id])
    away_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    away_team = db.relationship("Team", lazy=True, foreign_keys=[away_team_id])
    _game_time = db.Column("game_time", db.DateTime)

    @property
    def game_time(self):
        return self._game_time.isoformat() if self._game_time else ""

    @game_time.setter
    def game_time(self, game_time):
        self._game_time = datetime.fromisoformat(game_time)

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
