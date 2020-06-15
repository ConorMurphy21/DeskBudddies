import datetime

from prettytable import PrettyTable

from cmnSys.action import Action
from client.clientConfig import ClientConfig
from cmnSys.responseCode import ResponseCode
from cmnUtils import configManager
from cmnSys import directoryFinder, configInstance
from cmnUtils.dateUtils import string_to_datetime
from networking import tcpClient, packet as pct
from networking.packet import Packet


def main(args):
    settings = configInstance.clientConfig
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
    print(_parse_response(response))


def _add_response(response: Packet) -> str:
    data = response.data
    code = ResponseCode(data['responseCode'])
    if code == ResponseCode.OK:
        return "Successfully added you to the schedule!"
    elif code == ResponseCode.CONFLICT:
        return "Request denied due to these coworkers working this day: " + ', '.join(data['results'])
    elif code == ResponseCode.UNEXPECTED:
        return "You are already scheduled to work this day."
    elif code == ResponseCode.FORCED:
        return "You were successfully added to the schedule. Please notify: " + ', '.join(data['results'])
    elif code == ResponseCode.FORCE_FAILED:
        return "Unfortunately the server has disabled the force flag, and your request was denied due to these " \
               "coworkers working this day: " + ','.join(data['results'])
    elif code == ResponseCode.NOT_FOUND:
        return "There is no user id with the uid: " + data['results'][0] + ". Please contact your administrator."
    elif code == ResponseCode.FORBIDDEN:
        return "Something has gone terribly wrong."


def _remove_response(response: Packet) -> str:
    data = response.data
    code = ResponseCode(data['responseCode'])
    if code == ResponseCode.OK:
        return "Successfully removed you from the schedule!"
    elif code == ResponseCode.NOT_FOUND:
        return "You are not scheduled for this day and therefore do not need to be removed"
    elif code == ResponseCode.UNEXPECTED:
        return "Unsuccessfully removed you from the schedule."
    elif code == ResponseCode.NOT_FOUND:
        return "There is no user id with the uid: " + data['results'][0] + ". Please contact your administrator."
    elif code == ResponseCode.FORBIDDEN:
        return "Something has gone terribly wrong."


def _get_response(response: Packet) -> str:
    data = response.data
    code = ResponseCode(data['responseCode'])
    if code == ResponseCode.OK:
        if data['first_day']:
            table = PrettyTable()
            first_day = string_to_datetime(data['first_day'])

            for i in range(6):
                next_day = first_day + datetime.timedelta(days=i)
                uids_on_day = data['schedule'][i]
                if uids_on_day:
                    string = '\n'.join(uids_on_day)
                    table.add_column(next_day.strftime('%Y%m%d'), [string])

            return str(table)
        return "Successfully got uids from the schedule:" + ", ".join(data['results'])
    elif code == ResponseCode.UNEXPECTED:
        return "Unsuccessfully got uids from the schedule!"
    elif code == ResponseCode.FORBIDDEN:
        return "Something has gone terribly wrong."


def _parse_response(response: Packet) -> str:
    funcs = {Action.GET: _get_response,
             Action.REQUEST: _add_response,
             Action.REMOVE: _remove_response}
    return funcs[response.action](response)
