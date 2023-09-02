from dataclasses import dataclass
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db
from src.PickEmLeague.models.enums import GameResult, IntEnum
from src.PickEmLeague.models.user import User

from .game import Game

# TODO: Add databse validation on these records to prevent duplicates for user/game (unique index?)


@dataclass
class GamePick(db.Model):
    __tablename__ = "game_picks"
    id: int
    user: Mapped[User]
    game: Mapped[Game]
    pick: int
    amount: int

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", lazy=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = db.relationship("Game", lazy=True)
    pick = db.Column(IntEnum(GameResult), default=GameResult.NOT_PLAYED)
    amount = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "game_id": self.game_id,
            "pick": self.pick,
            "amount": self.amount,
        }

    @classmethod
    def find_by_id(cls, id: int) -> "GamePick":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_week(cls, week: int) -> List["GamePick"]:
        return db.session.scalars(
            select(cls).where(GamePick.game.has(Game.week == week))
        ).all()

    @classmethod
    def find_by_user_and_week(cls, user: User, week: int) -> List["GamePick"]:
        # return cls.query.filter((cls.user == user) & (cls.game.week == week)).all()
        user_picks = db.session.scalars(
            select(cls).where(cls.user == user).order_by(cls.amount)
        ).all()
        # print(user_picks)
        print("got user picks")
        results = [gp for gp in user_picks if gp.game.week == week]
        print("got results")
        # print(results)
        return results

    @classmethod
    def find_all(cls) -> List["GamePick"]:
        return cls.query.all()
