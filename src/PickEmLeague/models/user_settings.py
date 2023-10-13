from dataclasses import dataclass
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db
from src.PickEmLeague.models.user import User


@dataclass
class UserSettings(db.Model):
    __tablename__ = "user_settings"
    id: int
    user: Mapped[User]
    push_token: str

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    user = db.relationship("User", lazy=True, cascade="delete")
    push_token = db.Column(db.String)

    @classmethod
    def find_by_id(cls, id: int) -> "UserSettings":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user(cls, user: User) -> "UserSettings":
        return db.session.scalars(select(cls).where(cls.user == user)).first()

    @classmethod
    def find_all(cls) -> List["UserSettings"]:
        return cls.query.all()
