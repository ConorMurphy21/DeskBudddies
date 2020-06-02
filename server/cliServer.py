import os

from cmnUtils import directoryFinder
from cmnUtils.configManager import user_config_interface
from server.adjacencyMatrix import AdjacencyMatrix
from server.serverConfig import ServerConfig


def main(args):
    settings = ServerConfig(directoryFinder.server_config_file())
    if  not os.path.isfile("ServerAdjacencyMatrix.csv"):
        csv = input("An adjacency matrix from the csv has not been made, please provide an appropriate csv:")
        while True:
            try:
                adj = AdjacencyMatrix(csv)
                print(adj)
                break
            except FileNotFoundError:
                csv = input("The csv could not be opened, try again:")

    print("Unfortunately, we don't support querying the server because Python hates multithreading, so get all your "
          "configuration done now")
    user_config_interface(settings)
