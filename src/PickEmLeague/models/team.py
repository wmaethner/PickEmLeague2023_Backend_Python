from typing import List

from src.PickEmLeague import db


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    abbreviation = db.Column(db.String(10), nullable=False)
    conference = db.Column(db.String(3), nullable=False)
    division = db.Column(db.String(5), nullable=False)

    @classmethod
    def find_by_id(cls, id: int) -> "Team":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_abbreviation(cls, abbr: str) -> "Team":
        return cls.query.filter_by(abbreviation=abbr).first()

    @classmethod
    def find_all(cls) -> List["Team"]:
        return cls.query.all()
