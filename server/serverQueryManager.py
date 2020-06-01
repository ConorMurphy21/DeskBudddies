
# These are all of the methods callable by the client, that interact with the server
from cli.action import Action
from networking.packets.packet import Packet


def add(args: dict) -> dict:
    response = {}

    return response


def remove(args: dict) -> dict:
    response = {}

    return response


def get(args: dict) -> dict:
    response = {}

    return response


FUNCS = {Action.QUERY: add,
         Action.REMOVE: remove,
         Action.GET: get}


def respond(packet: Packet) -> Packet:
    return Packet(packet.action, FUNCS[packet.action](packet.data))
