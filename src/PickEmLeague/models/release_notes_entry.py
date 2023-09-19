from dataclasses import dataclass
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Mapped

from src.PickEmLeague import db


@dataclass
class ReleaseNotesEntry(db.Model):
    __tablename__ = "release_notes_entry"
    id: int
    entry: str

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entry = db.Column(db.String, nullable=False)
    release_notes_id = db.Column(
        db.Integer, db.ForeignKey("release_notes.id", ondelete="CASCADE")
    )

    @classmethod
    def find_by_id(cls, id: int) -> "ReleaseNotesEntry":
        return cls.query.filter_by(id=id).first()
