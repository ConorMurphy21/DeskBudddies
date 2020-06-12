from cli import argsParser
from cmnSys.action import Action
from client import cliClient
from server import cliServer


def main():
    args = argsParser.parse_args()
    if args:
        if args.action.client_action():
            cliClient.main(args)
        else:
            cliServer.main(args)


if __name__ == "__main__":
    main()
