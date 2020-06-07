from cmnSys.action import Action
from client.clientConfig import ClientConfig
from cmnUtils import configManager
from cmnSys import directoryFinder
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
    print("It looks like this is your first time using it. For now we will just configure some essentials, but you can"
          " use the config flag to customize further.")
    host = input("Please enter the hostname or ip of your DeskBuddies server: ")
    uid = input("Please enter your user id: ")
    settings['host'] = host
    settings['uid'] = uid
    settings.write()


def _config(settings):
    configManager.user_config_interface(settings)
    settings.write()


def _ask_server(args, settings):
    # just in case any required info for the packet creation is configured (like uid)
    args = {**args, **settings.data}
    packet = pct.from_args(args)
    response = tcpClient.send_packet(packet, settings['host'], settings['port'])
    print(response.encode().decode('utf-8'))
    print(_parse_response(response))


def _parse_response(response: Packet) -> str:
    pass
