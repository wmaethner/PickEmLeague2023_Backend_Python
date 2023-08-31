from typing import Any, List

from flask_restx import Namespace


class BaseNamespace(Namespace):
    def add_models(self, models: List[Any]):
        for model in models:
            self.add_model(model.name, model)
