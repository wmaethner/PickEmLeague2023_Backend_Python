from dataclasses import dataclass
from datetime import datetime
from typing import List

from sqlalchemy import asc, desc, select
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db
from src.PickEmLeague.models.user import User


@dataclass
class Message(db.Model):
    __tablename__ = "messages"
    id: int
    user: Mapped[User]
    text: str
    created_at: Mapped[datetime]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", lazy=True)
    text = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def find_by_id(cls, id: int) -> "Message":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["Message"]:
        return db.session.scalars(select(cls).order_by(desc(cls.created_at))).all()

    # @classmethod
    # def find_by_user(cls, user: User) -> List["Message"]:
    #     return db.paginate(select(cls).where(cls.user == user))
