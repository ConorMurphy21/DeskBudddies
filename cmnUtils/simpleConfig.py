import json


class SimpleConfig:

    def __init__(self):
        self.props = None

    def set_props(self):
        self.props = vars(self)

    def to_json(self) -> str:
        self.set_props()
        return json.dumps(self.props)

    def from_json(self, json_str: str):
        pass


def to_dict(json_str: str) -> dict:
    return json.loads(json_str)

