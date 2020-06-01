from cli.action import Action
from client.clientConfig import ClientConfig
from cmnUtils import directoryFinder


def main(args):
    settings = ClientConfig(directoryFinder.client_config_file())
    if args.action == Action.CONFIG:
        config(settings)
        return

    if settings['host'] == '' or settings['ip'] == '':
        required_config(settings)
    ask_server(args, settings)


def required_config(settings):
    print("It looks like this is your first time using it.")
    host = input("Please enter the hostname or ip of your DeskBuddies server: ")
    uid = input("Please enter your user id: ")
    settings['host'] = host
    settings['uid'] = uid


def config(settings):
    pass


def ask_server(args, settings):
    pass
