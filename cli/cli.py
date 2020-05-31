from networking import tcpClient
from networking.tcpServer import TcpServer


def main():
    # parse commandline argument, and pass to respective cli's
    server = TcpServer(6719)
    server.run()
    tcpClient.send_packet("hello", "localhost", 6719)
    return
    """
    args = argumentsParser.parse_args()
    if args:
        if args.action == Action.SERVE:
            cliServer.main(args)
        else:
            cliClient.main(args)
    """


if __name__ == "__main__":
    main()
