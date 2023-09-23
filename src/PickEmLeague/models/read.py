from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db


class Readables:
    RELEASE_NOTES = 1


@dataclass
class Read(db.Model):
    __tablename__ = "reads"
    id: int
    readable: int
    readable_id: int
    user_id: int
    read_at: Mapped[datetime]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    readable = db.Column(db.Integer, index=True)
    readable_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    read_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def find_by_id(cls, id: int) -> "Read":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user_and_type(cls, user_id: int, readable_type: int) -> List["Read"]:
        return db.session.scalars(
            select(cls)
            .where(cls.user_id == user_id)
            .where(cls.readable == readable_type)
        ).all()

    @classmethod
    def find_by_user_and_type_agg_ids(
        cls, user_id: int, readable_type: int
    ) -> List[int]:
        return db.session.scalars(
            select(cls.readable_id)
            .where(cls.user_id == user_id)
            .where(cls.readable == readable_type)
            .group_by(cls.readable_id)
        ).all()

    @classmethod
    def find_by_user_and_readable(
        cls, user_id: int, readable_type: int, readable_id
    ) -> "Read":
        return db.session.scalars(
            select(cls)
            .where(cls.user_id == user_id)
            .where(cls.readable == readable_type)
            .where(cls.readable_id == readable_id)
        ).first()
