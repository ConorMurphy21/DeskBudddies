from enum import IntEnum


class ResponseCode(IntEnum):
    OK = 200
    CONFLICT = 409
    UNEXPECTED = 417
    NOT_FOUND = 404
    FORBIDDEN = 403
    FORCED = 405
    FORCE_FAILED = 406
