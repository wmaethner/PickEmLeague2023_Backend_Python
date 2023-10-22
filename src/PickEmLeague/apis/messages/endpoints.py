from flask import g
from flask_restx import Resource

from src.PickEmLeague.decorators.auth import login_required
from src.PickEmLeague.schemas.messages.message_schema import (
    last_message_read_model,
    last_message_read_schema,
    message_list_model,
    message_model,
    message_schema,
)

from ..core.base_namespace import BaseNamespace
from .business import add_message, get_all, get_read, update_read
from .parsers import new_message_parser

messages_ns = BaseNamespace(name="messages", validate=True)
messages_ns.add_models([message_schema, message_model, message_list_model])


@messages_ns.route("")
class MessageList(Resource):
    @messages_ns.marshal_with(message_list_model)
    def get(self):
        return get_all()

    @login_required
    @messages_ns.expect(new_message_parser)
    @messages_ns.doc(security="Bearer")
    def post(self):
        args = new_message_parser.parse_args()
        add_message(args["text"], g.user.id)


@messages_ns.route("/read")
class LastMessageRead(Resource):
    @login_required
    @messages_ns.doc(security="Bearer")
    @messages_ns.marshal_with(last_message_read_model)
    def get(self):
        return get_read(g.user.id)


@messages_ns.route("/<int:id>/read")
class ReadMessage(Resource):
    @login_required
    @messages_ns.doc(security="Bearer")
    def put(self, id):
        print("update read")
        print(g.user)
        return update_read(id, g.user.id)
