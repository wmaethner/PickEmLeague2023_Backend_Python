from datetime import date

from src.PickEmLeague import db
from src.PickEmLeague.models.read import Read, Readables
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


def add_read(release_notes_id, user_id):
    read = Read(
        readable=Readables.RELEASE_NOTES, readable_id=release_notes_id, user_id=user_id
    )
    db.session.add(read)
    db.session.commit()


def get_reads(user_id):
    return BaseModel.SuccessResult(
        {"ids": Read.find_by_user_and_type_agg_ids(user_id, Readables.RELEASE_NOTES)}
    )
