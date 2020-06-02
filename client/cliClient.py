from cli.action import Action
from client.clientConfig import ClientConfig
from cmnUtils import directoryFinder
from networking import tcpClient
from networking.packets import packet as pct
from networking.packets.packet import Packet


def main(args):
    settings = ClientConfig(directoryFinder.client_config_file())
    if args.action == Action.CONFIG:
        _config(settings)
        return

    if settings['host'] == '' or settings['uid'] == '':
        _required_config(settings)
    _ask_server(vars(args), settings)


def _required_config(settings):
    print("It looks like this is your first time using it.")
    host = input("Please enter the hostname or ip of your DeskBuddies server: ")
    uid = input("Please enter your user id: ")
    settings['host'] = host
    settings['uid'] = uid
    settings.write()


def _config(settings):
    pass


def _ask_server(args, settings):
    # just in case any required info for the packet creation is configured (like uid)
    args = {**args, **vars(settings)}
    packet = pct.from_args(args)
    response = tcpClient.send_packet(packet, settings['host'], settings['port'])
    print(_parse_response(response))


def _parse_response(response: Packet) -> str:
    pass
