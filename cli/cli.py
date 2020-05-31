from cli import argumentsParser
from cli.action import Action
from client import cliClient
from server import cliServer


def main():
    # parse commandline argument, and pass to respective cli's
    args = argumentsParser.parse_args()
    if args:
        if args.action == Action.SERVE:
            cliServer.main(args)
        else:
            cliClient.main(args)


if __name__ == "__main__":
    main()
