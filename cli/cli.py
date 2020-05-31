from multiprocessing import Process

from networking import tcpClient
from networking.tcpServer import TcpServer


def main():
    server = TcpServer(6719)
    server.run()
    tcpClient.send_packet("hello", '127.0.0.1', 6719)


if __name__ == "__main__":
    main()
