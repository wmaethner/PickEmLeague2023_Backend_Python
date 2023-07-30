from typing import List

from src.PickEmLeague import db
from src.PickEmLeague.models.enums import GameResult, IntEnum
from src.PickEmLeague.models.user import User

from .game import Game

# TODO: Add databse validation on these records to prevent duplicates for user/game (unique index?)


class GamePick(db.Model):
    __tablename__ = "game_picks"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", lazy=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = db.relationship("Game", lazy=True)
    pick = db.Column(IntEnum(GameResult), default=GameResult.NOT_PLAYED)
    amount = db.Column(db.Integer)

    @classmethod
    def find_by_id(cls, id: int) -> "GamePick":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_week(cls, week: int) -> List["GamePick"]:
        return cls.query.filter(cls.game.week == week).all()

    @classmethod
    def find_by_user_and_week(cls, user: User, week: int) -> List["GamePick"]:
        return cls.query.filter(cls.user == user, cls.game.week == week).all()

    @classmethod
    def find_all(cls) -> List["GamePick"]:
        return cls.query.all()
