import os

from cmnSys import directoryFinder
from cmnSys.action import Action
from cmnUtils.configManager import user_config_interface
from networking.tcpServer import TcpServer
from server.adjacencyMatrix import AdjacencyMatrix
from server.serverConfig import ServerConfig
from server.serverQueryManager import ServerQueryManager


def main(args):
    # get settings
    settings = ServerConfig(directoryFinder.server_config_file())
    # get adjacency file up to date
    if args.action == Action.IMPORT:
        import_adj(args.adj)
    elif args.action == Action.SERVCFG:
        user_config_interface(settings)
    else:
        if not directoryFinder.server_adjacency_file().is_file():
            print("No adjacency file found, please use the import flag to import an adjacency file.")
            return

        print("Server is now running.")
        TcpServer(settings['port']).run(ServerQueryManager())


def get_adjmat() -> AdjacencyMatrix:
    csv = input("Please provide a path to your adjacency file here: ")
    while True:
        adj = try_get_adj(csv)
        if not adj:
            csv = input("The file provided could not be opened. Please try again:")
        else:
            break
    return adj


def import_adj(csv: str):
    adj = try_get_adj(csv)
    if not adj:
        if os.path.isfile(csv):
            print("Your adjacency file does not follow the expected format of an adjacency matrix!")
        else:
            print("Could not find: " + csv)
    else:
        adj.write_to_csv(directoryFinder.server_adjacency_file())
        print("Successfully imported adjacency file: " + csv)


def try_get_adj(csv: str):
    try:
        return AdjacencyMatrix(csv)
    except FileNotFoundError:
        return None
