# These are all of the methods callable by the client, that interact with the server
import datetime


from cmnSys.action import Action
from cmnSys import directoryFinder, configInstance
from cmnSys.responseCode import ResponseCode
from cmnUtils.dateUtils import string_to_datetime, get_week
from networking.packet import Packet
from server.adjacencyMatrix import AdjacencyMatrix
from server.schedule import Schedule


class ServerQueryManager:

    def __init__(self):
        self.funcs = {Action.GET: self.get,
                      Action.REMOVE: self.remove,
                      Action.REQUEST: self.add}

        self.schedule = Schedule(directoryFinder.server_schedule_dir())
        self.adjmat = AdjacencyMatrix(directoryFinder.server_adjacency_file())
        self.settings = configInstance.serverConfig

    def add(self, args: dict) -> dict:
        datetime_obj = string_to_datetime(args['date'])
        results = []
        uids_on_day = self.schedule.get(datetime_obj)
        response_code = ResponseCode.FORBIDDEN

        if not self.adjmat.includes(args['uid']):
            # uid not in adjacency matrix
            response_code = ResponseCode.NOT_FOUND
            results.append(args['uid'])
        else:
            for uid in uids_on_day:
                if self.adjmat.is_adjacent(args['uid'], uid):
                    results.append(uid)

            if len(results) > 0:
                # uid can't work on the same day as someone already working on that day
                if self.settings['enableForce'] and args['force']:
                    added = self.schedule.add(args['uid'], datetime_obj)
                    if not added:
                        # uid not added successfully
                        response_code = ResponseCode.UNEXPECTED
                    else:
                        # uid added to day successfully
                        response_code = ResponseCode.FORCED
                elif args['force']:
                    response_code = ResponseCode.FORCE_FAILED
                else:
                    response_code = ResponseCode.CONFLICT

            else:
                added = self.schedule.add(args['uid'], datetime_obj)
                if not added:
                    # uid not added successfully
                    response_code = ResponseCode.UNEXPECTED
                else:
                    # uid added to day successfully
                    response_code = ResponseCode.OK

        response = {'responseCode': response_code, 'results': results}
        return response

    def remove(self, args: dict) -> dict:
        datetime_obj = string_to_datetime(args['date'])
        response_code = ResponseCode.FORBIDDEN
        results = []

        if not self.adjmat.includes(args['uid']):
            # uid not in adjacency matrix
            response_code = ResponseCode.NOT_FOUND
            results.append(args['uid'])
        else:
            uids_on_day = self.schedule.get(datetime_obj)
            count = uids_on_day.count(args['uid'])

            if count == 0:
                # uid not found on day
                response_code = ResponseCode.NOT_FOUND
            else:
                self.schedule.remove(args['uid'], datetime_obj)
                # uid removed from day successfully
                response_code = ResponseCode.OK

                check = self.schedule.get(datetime_obj)
                count = check.count(args['uid'])

            if count != 0:
                # uid was not removed correctly, expectation failed
                response_code = ResponseCode.UNEXPECTED

        response = {'responseCode': response_code, 'results': results}
        return response

    def get(self, args: dict) -> dict:
        datetime_obj = string_to_datetime(args['date'])
        response_code = ResponseCode.FORBIDDEN
        results = {}
        schedule = []
        first_day = ''
        if args['week']:
            first_day = get_week(datetime_obj, True)
            week = []
            i = 0
            while i < 7:
                next_day = first_day + datetime.timedelta(days=i)
                schedule.append(self.schedule.get(next_day))
                i += 1
            response_code = ResponseCode.OK
            first_day = first_day.strftime('%Y%m%d')
        else:
            results = self.schedule.get(datetime_obj)
            # uids on date gotten successfully
            response_code = ResponseCode.OK

        response = {'responseCode': response_code, 'first_day': first_day, 'results': results, 'schedule': schedule}
        return response

    def respond(self, packet: Packet) -> Packet:
        args = packet.data
        return Packet(packet.action, self.funcs[packet.action](args))
