
# These are all of the methods callable by the client, that interact with the server
from cli.action import Action
from cmnUtils import directoryFinder
from networking.packets.packet import Packet
from server.schedule import Schedule


class ServerQueryManager:

    def __init__(self):
        self.funcs = {Action.GET: self.get,
                      Action.REMOVE: self.remove,
                      Action.QUERY: self.add}

        self.schedule = Schedule(directoryFinder.server_schedule_dir())
        self.adjmat = Schedule(directoryFinder.server_adjacency_file())

    def add(self, args: dict) -> dict:
        response = {'success': True}

        return response

    def remove(self, args: dict) -> dict:
        response = {}

        return response

    def get(self, args: dict) -> dict:
        response = {}

        return response

    def respond(self, packet: Packet) -> Packet:
        args = packet.data
        return Packet(packet.action, self.funcs[packet.action](args))
