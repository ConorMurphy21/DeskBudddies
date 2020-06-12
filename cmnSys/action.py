from enum import IntEnum


class Action(IntEnum):
    # All serve actions come first, if you add an action
    # change client action accordingly
    SERVCFG = 0
    IMPORT = 1
    SERVE = 2
    CONFIG = 3
    REQUEST = 4
    REMOVE = 5
    GET = 6

    def client_action(self) -> bool:
        return self.value > 2

    def requires_date(self) -> bool:
        return self.value > self.CONFIG
