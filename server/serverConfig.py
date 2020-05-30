from cmnUtils.simpleConfig import SimpleConfig


class ServerConfig(SimpleConfig):

    # this object acts as a data class, that can be converted to and from JSON easily for storage
    # any complex objects that need to be stored, can be stored via links to other files
    # and an override of these properties get and set functionality
    def __init__(self):
        super().__init__()
        self.adjacencyFile = None
        self.scheduleFile = None
