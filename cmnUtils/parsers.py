FALSE_STRS = ['false', '0', 'no', 'n', 'negative']
TRUE_STRS = ['true', '1', 'yes', 'y', 'affirmative']


def parse_bool(val: str) -> bool:
    if val not in FALSE_STRS and val not in TRUE_STRS:
        raise ValueError()
    else:
        return val in TRUE_STRS
