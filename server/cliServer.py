import os

from cmnSys import directoryFinder
from cmnSys.action import Action
from cmnUtils.configManager import user_config_interface
from networking.tcpServer import TcpServer
from server.adjacencyMatrix import AdjacencyMatrix
from server.serverConfig import ServerConfig


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
            get_adjmat().write_to_csv(directoryFinder.server_adjacency_file())
        else:
            if input("Would you like to update or change your adjacency file (y/n):") == 'y':
                get_adjmat().write_to_csv(directoryFinder.server_adjacency_file())

        user_config_interface(settings)

        # runs server in another thread
        TcpServer(settings['port']).run()


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
    adj.write_to_csv(directoryFinder.server_adjacency_file())
    print("Successfully imported adjacency file: ")


def try_get_adj(csv: str):
    try:
        return AdjacencyMatrix(csv, False)
    except FileNotFoundError:
        return None
