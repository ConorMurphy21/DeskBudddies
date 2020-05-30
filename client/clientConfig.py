from cmnUtils import simpleConfig
from cmnUtils.simpleConfig import SimpleConfig


class ClientConfig(SimpleConfig):

    # this object acts as a data class, that can be converted to and from JSON easily for storage
    # any complex objects that need to be stored, can be stored via links to other files
    # and an override of these properties get and set functionality
    def __init__(self):
        super().__init__()
        self.serverIp = None
        self.uid = None

    def from_json(self, json_str: str):
        self.props = simpleConfig.to_dict(json_str)
        self.serverIp = self.props['serverIp']
        self.uid = self.props['uid']
