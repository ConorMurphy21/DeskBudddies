from cli.action import Action
from client.clientConfig import ClientConfig
from cmnUtils import directoryFinder


def main(args):
    settings = ClientConfig(directoryFinder.client_config_file())
    if args.action == Action.CONFIG:
        config(settings)
    elif settings['host'] == '' or settings['ip'] == '':
        required_config(settings)
    else:
        ask_server(args, settings)


def required_config(settings):
    pass


def config(settings):
    pass


def ask_server(args, settings):
    pass
