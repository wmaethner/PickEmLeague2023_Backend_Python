from flask import Response, jsonify
from flask_restx import Model
from flask_restx.fields import Boolean, Nested, String


class BaseModel:
    def __init__(self, name: str, dataModel: Model) -> None:
        self.name = name
        self.dataModel = dataModel

    def model(self) -> Model:
        return Model(
            self.name,
            {"success": Boolean, "message": String, "data": Nested(self.dataModel)},
        )

    @classmethod
    def SuccessResult(cls, data: {}, message="") -> Response:
        return jsonify({"success": True, "message": message, "data": data}).json

    @classmethod
    def ErrorResult(cls, message: str) -> Response:
        return jsonify({"success": False, "message": message}).json
