from flask import g
from flask_restx import Resource

from src.PickEmLeague.decorators.auth import login_required
from src.PickEmLeague.schemas.reads.reads_schema import read_ids_model, read_ids_schema
from src.PickEmLeague.schemas.release_notes.release_notes_schema import (
    entry_schema,
    release_notes_list_model,
    release_notes_model,
    release_notes_schema,
)

from ..core.base_namespace import BaseNamespace
from .business import (
    add_entry,
    add_read,
    create_release_note,
    get_all_release_notes,
    get_reads,
    get_release_notes_by_id,
)
from .parsers import release_notes_entry_parser, release_notes_parser

release_notes_ns = BaseNamespace(name="release_notes", validate=True)
release_notes_ns.add_models(
    [
        entry_schema,
        release_notes_schema,
        release_notes_model,
        release_notes_list_model,
        read_ids_schema,
        read_ids_model,
    ]
)


@release_notes_ns.route("/<int:id>")
class ReleaseNotesById(Resource):
    @release_notes_ns.marshal_with(release_notes_model)
    def get(self, id):
        return get_release_notes_by_id(id)

    # Add entry
    @release_notes_ns.expect(release_notes_entry_parser)
    def put(self, id):
        args = release_notes_entry_parser.parse_args()
        add_entry(id, args["entry"])


@release_notes_ns.route("")
class ReleaseNotesList(Resource):
    @release_notes_ns.marshal_with(release_notes_list_model)
    def get(self):
        """Retrieve a list of games."""
        return get_all_release_notes()

    @release_notes_ns.expect(release_notes_parser)
    def post(self):
        args = release_notes_parser.parse_args()
        create_release_note(args["title"], args["date"])
        return {}


@release_notes_ns.route("/reads/<int:id>")
class ReleaseNotesRead(Resource):
    @login_required
    @release_notes_ns.doc(security="Bearer")
    def post(self, id):
        print(f"Release ntoes read post: {id}")
        return add_read(id, g.user.id)


@release_notes_ns.route("/reads")
class ReleaseNotesReads(Resource):
    @login_required
    @release_notes_ns.doc(security="Bearer")
    @release_notes_ns.marshal_with(read_ids_model)
    def get(self):
        return get_reads(g.user.id)
