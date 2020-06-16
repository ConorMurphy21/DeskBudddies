from cmnSys.simpleConfig import SimpleConfig
from cmnUtils import parsers


class ServerConfig(SimpleConfig):
    def set_default_data(self):
        self.data = {
            'port': 6719,
            'enableForce': False
        }

    def set_parse_funcs(self):
        self.parsers = {
            'enableForce': parsers.parse_bool
        }

