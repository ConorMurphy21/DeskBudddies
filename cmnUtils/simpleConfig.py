import json
from collections import UserDict


class SimpleConfig(UserDict):

    def __init__(self, json_file_path):
        self.set_default_data()
        with open(json_file_path) as json_file:
            client_set = json.load(json_file)
            for key, val in client_set:
                self.data[key] = val

    def to_json(self) -> str:
        return json.dumps(self.data)

    def set_default_data(self):
        pass
