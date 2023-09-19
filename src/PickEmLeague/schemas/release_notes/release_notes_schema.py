from flask_restx import Model
from flask_restx.fields import Date, Integer, List, Nested, String

from ..core.base_schema import BaseModel

entry_schema = Model("EntrySchema", {"entry": String})

release_notes_schema = Model(
    "ReleaseNotesSchema",
    {
        "id": Integer,
        "title": String,
        "date": Date,
        "entries": List(Nested(entry_schema)),
    },
)

release_notes_model = BaseModel("ReleaseNotesModel", release_notes_schema).model()
release_notes_list_model = BaseModel(
    "ReleaseNotesListModel", release_notes_schema
).list_model()
