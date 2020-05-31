import argparse
from datetime import datetime

from cli.action import Action

WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
            'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']


def parse_args():
    parser = argparse.ArgumentParser(
        description='Communicate who can come into the office while maintaining social distancing')
    parser.add_argument("-s", "--serve", action="store_true", help="Run a DeskBuddies server")
    parser.add_argument("-q", "--query", action="store_true", help="Request to work (Requires date or day)")
    parser.add_argument("-r", "--remove", action="store_true", help="Remove request to work (Requires date or day)")
    parser.add_argument("-g", "--get", action="store_true", help="Request schedule (Requires date or day)")
    parser.add_argument("-w", "--week", action="store_true", help="Request a week of schedule")
    parser.add_argument("-p", "--config", action="store_true", help="Update client configuration properties")
    parser.add_argument("-c", "--date", type=str,
                        help="Calendar date in the form dd/mm, (format is configurable)")
    parser.add_argument("-d", "--day", type=str, help="Weekday (full or abbreviated)", choices=WEEKDAYS)
    parser.add_argument("--action", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if not parse_and_validate(args):
        return None

    return args


def parse_and_validate(args) -> bool:
    no_date = False
    if args.day and args.date:
        return False
    elif args.day:
        args.day = WEEKDAYS.index(args.day) % 7
    elif args.date:
        args.date = datetime.strptime(args.date, "%d/%m")
    else:
        no_date = True

    actions = ['serve', 'config', 'query', 'remove', 'get']
    args_dict = vars(args)
    num = 0
    # default action is get
    args.action = Action.QUERY
    for action in actions:
        if args_dict[action]:
            num += 1
            args.action = Action(actions.index(action))

    # should only have 1 action
    if num > 1:
        return False

    if args.action > Action.CONFIG and no_date:
        return False

    return True
