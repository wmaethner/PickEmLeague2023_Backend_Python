from dataclasses import dataclass
from typing import List

from sqlalchemy import desc, select
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db
from src.PickEmLeague.models.enums import GameResult, IntEnum
from src.PickEmLeague.models.user import User

from .game import Game


@dataclass
class GamePick(db.Model):
    __tablename__ = "game_picks"
    id: int
    user: Mapped[User]
    game: Mapped[Game]
    pick: int
    amount: int

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    user = db.relationship("User", lazy=True, cascade="delete")
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = db.relationship("Game", lazy=True)
    pick = db.Column(IntEnum(GameResult), default=GameResult.NOT_PLAYED)
    amount = db.Column(db.Integer)

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
        return db.session.scalars(
            select(cls)
            .where(cls.user == user)
            .where(GamePick.game.has(Game.week == week))
            .order_by(desc(cls.amount))
        ).all()

    @classmethod
    def find_by_user(cls, user: User) -> List["GamePick"]:
        return db.session.scalars(
            select(cls).where(cls.user == user).order_by(desc(cls.amount))
        ).all()

    @classmethod
    def find_by_game(cls, game: Game) -> List["GamePick"]:
        return db.session.scalars(select(cls).where(cls.game == game)).all()

    @classmethod
    def find_all(cls) -> List["GamePick"]:
        return cls.query.all()
