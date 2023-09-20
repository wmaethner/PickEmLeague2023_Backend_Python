from dataclasses import dataclass
from datetime import date, datetime
from typing import List

from sqlalchemy import desc, select
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db
from src.PickEmLeague.models.release_notes_entry import ReleaseNotesEntry


@dataclass
class ReleaseNotes(db.Model):
    __tablename__ = "release_notes"
    id: int
    title: str
    entries: Mapped[List[ReleaseNotesEntry]]
    date: str

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title: str = db.Column(db.String(255))
    entries = db.relationship("ReleaseNotesEntry", backref="release_notes")
    _date = db.Column("date", db.DateTime)

    @property
    def date(self):
        return self._date.strftime("%Y-%m-%d") if self._date else ""

    @date.setter
    def date(self, date_str):
        self._date = datetime.strptime(date_str, "%Y-%m-%d").date()

    @classmethod
    def find_by_id(cls, id: int) -> "ReleaseNotes":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["ReleaseNotes"]:
        return db.session.scalars(select(cls).order_by(desc(cls.id))).all()
