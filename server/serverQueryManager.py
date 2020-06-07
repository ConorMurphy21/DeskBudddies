
# These are all of the methods callable by the client, that interact with the server
from cli.action import Action
from cmnUtils import directoryFinder
from cmnUtils.dateUtils import string_to_datetime
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
        print(directoryFinder.server_adjacency_file())
        print(directoryFinder.server_schedule_dir())

        datetime_obj = string_to_datetime(args['date'])
        results = []
        uids_on_day = self.schedule.get(datetime_obj)
        adjacency = False
        for uid in uids_on_day:
            adjacency = self.adjmat.is_adjacent(args['uid'], uid)
            results.append(uid)

            if uid == args['uid']:
                adjacency = True
                results = "Already requested to work on that day"

        if not adjacency:
            # uid added to day successfully
            response_code = 200
        else:
            # conflict (can't work on same day as someone scheduled for that day)
            response_code = 409

        response = {'responseCode': response_code, 'results': results}

        return response

    def remove(self, args: dict) -> dict:
        datetime_obj = string_to_datetime(args['date'])
        results = []
        uids_on_day = self.schedule.get(datetime_obj)

        count = uids_on_day.count(args['uid'])
        if count == 0:
            # uid not found on day
            response_code = 404
        else:
            self.schedule.remove(args['uid'], datetime_obj)
            # uid removed from day successfully
            response_code = 200

            results = self.schedule.get(datetime_obj)
            count = results.count(args['uid'])

        if count != 0:
            # uid was not removed correctly, expectation failed
            response_code = 417

        response = {'responseCode': response_code, 'results': results}

        return response

    def get(self, args: dict) -> dict:
        response = {}

        return response

    def respond(self, packet: Packet) -> Packet:
        args = packet.data
        return Packet(packet.action, self.funcs[packet.action](args))
