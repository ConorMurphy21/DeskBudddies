from cmnUtils import simpleConfig
from cmnUtils.simpleConfig import SimpleConfig


class ClientConfig(SimpleConfig):

    def set_default_data(self):
        self.data = {
            'host': '',
            'uid': '',
        }
