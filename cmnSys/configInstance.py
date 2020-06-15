from client.clientConfig import ClientConfig
from cmnSys import directoryFinder
from server.serverConfig import ServerConfig

serverConfig = ServerConfig(directoryFinder.server_config_file())
clientConfig = ClientConfig(directoryFinder.client_config_file())


