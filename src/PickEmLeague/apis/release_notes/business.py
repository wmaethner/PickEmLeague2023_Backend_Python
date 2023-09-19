from datetime import date

from src.PickEmLeague import db
from src.PickEmLeague.models.release_notes import ReleaseNotes
from src.PickEmLeague.models.release_notes_entry import ReleaseNotesEntry
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def get_all_release_notes():
    return BaseModel.SuccessResult(ReleaseNotes.find_all())


def get_release_notes_by_id(id: int):
    return BaseModel.SuccessResult(ReleaseNotes.find_by_id(id))


def create_release_note(title: str, date_str: str):
    release_note = ReleaseNotes(title=title, date=date_str)
    db.session.add(release_note)
    db.session.commit()


def add_entry(release_notes_id, entry):
    release_note_entry = ReleaseNotesEntry(
        release_notes_id=release_notes_id, entry=entry
    )
    db.session.add(release_note_entry)
    db.session.commit()
