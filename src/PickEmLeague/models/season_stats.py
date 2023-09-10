from dataclasses import dataclass
from typing import List

from sqlalchemy import desc, select
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db
from src.PickEmLeague.models.user import User


@dataclass
class SeasonStats(db.Model):
    __tablename__ = "season_stats"
    id: int
    user: Mapped[User]
    score: int
    correct_picks: int

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    user = db.relationship("User", lazy=True, cascade="delete")
    score: int = db.Column(db.Integer)
    correct_picks: int = db.Column(db.Integer)

    @classmethod
    def find_by_id(cls, id: int) -> "SeasonStats":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user(cls, user: User) -> List["SeasonStats"]:
        return db.session.scalars(
            select(cls).where(cls.user == user).order_by(desc(cls.score))
        ).all()

    @classmethod
    def find_all(cls) -> List["SeasonStats"]:
        return cls.query.all()
