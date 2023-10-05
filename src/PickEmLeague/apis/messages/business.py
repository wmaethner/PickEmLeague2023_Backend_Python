from datetime import datetime

from src.PickEmLeague import db
from src.PickEmLeague.models.message import Message
from src.PickEmLeague.models.read import Read, Readables
from src.PickEmLeague.schemas.core.base_schema import BaseModel


def get_all():
    return BaseModel.SuccessResult(Message.find_all())


def add_message(message: str, user_id):
    message = Message(user_id=user_id, text=message)
    db.session.add(message)
    db.session.commit()


def update_read(message_id, user_id):
    print(message_id)
    print(user_id)
    reads = Read.find_by_user_and_type(user_id, Readables.MESSAGES)
    print(reads)
    if not reads:
        read = Read(readable=Readables.MESSAGES, readable_id=message_id, user_id=user_id)
        db.session.add(read)
    else:
        read = reads[0]
    print(read)
    read.readable_id = message_id
    read.read_at = datetime.utcnow()
    print(read)
    db.session.commit()
    print("done")


def get_read(user_id):
    print("GET READ")
    reads = Read.find_by_user_and_type(user_id, Readables.MESSAGES)
    if not reads:
        read = Read(readable=Readables.MESSAGES, readable_id=0, user_id=user_id)
        db.session.add(read)
        db.session.commit()
        return BaseModel.SuccessResult(read)
    else:
        return BaseModel.SuccessResult(reads[0])
