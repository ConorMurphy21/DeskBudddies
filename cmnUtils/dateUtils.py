import datetime


def get_next_weekday(weekday: int) -> datetime:
    today = datetime.date.today()
    weekday = today + datetime.timedelta((weekday - today.weekday()) % 7)
    # make sure to zero the time
    return datetime.datetime(weekday.year, weekday.month, weekday.day)


def string_to_datetime(string_date) -> datetime:
    return datetime.datetime.strptime(string_date, '%Y%m%d')


def get_week(weekday: datetime, mondayfirstday: bool) -> datetime:
    if mondayfirstday:
        weekday -= datetime.timedelta(days=weekday.weekday())
    else:
        day = weekday.weekday()
        if day <= 5:
            day += 1
        else:
            day = 0
        weekday -= datetime.timedelta(days=day)
    return datetime.datetime(weekday.year, weekday.month, weekday.day)


def validate_date_format(format_str: str) -> bool:
    #  tests date string format and returns false if its lacking info
    result = _format_type(format_str)
    if result == 0:
        return False
    else:
        return True


def _format_type(date_format: str) -> int:
    expected1 = datetime.datetime(2018, 2, 2)
    expected2 = datetime.datetime(2001, 3, 15)
    actual1 = datetime.datetime.strptime(expected1.strftime(date_format), date_format)
    actual2 = datetime.datetime.strptime(expected2.strftime(date_format), date_format)
    has_year = actual1.year == expected1.year and actual2.year == expected2.year
    has_month = actual1.month == expected1.month and actual2.month == expected2.month
    has_day = actual1.day == expected1.day and actual2.day == expected2.day
    if has_year and has_month and has_day:
        return 3
    elif has_month and has_day:
        return 2
    elif has_day and not has_year:
        return 1
    else:
        return 0


def parse_date_str(date_str: str, format_str: str) -> datetime:
    true_date = datetime.datetime.now()
    true_date = datetime.datetime(true_date.year, true_date.month, true_date.day)
    parsed_date = datetime.datetime.strptime(date_str, format_str)
    type_date_format = _format_type(format_str)

    if type_date_format == 0:  # should never happen as date format str is validated beforehand
        raise ValueError("Unable to parse from improper date format")
    if type_date_format == 1:  # only day is given
        parsed_date = datetime.datetime(true_date.year, true_date.month, parsed_date.day)
        if parsed_date < true_date:  # if day has passed its next month
            parsed_date = parsed_date.replace(month=parsed_date.month + 1)
    if type_date_format == 2:  # only day month is given
        parsed_date = parsed_date.replace(year=true_date.year)
        if parsed_date < true_date:  # if greater then go back one year
            parsed_date = parsed_date.replace(year=true_date.year + 1)

    fixed_parsed_date = datetime.datetime(parsed_date.year, parsed_date.month, parsed_date.day)
    if fixed_parsed_date < true_date:  # requested day is in the past
        raise ValueError()
    return fixed_parsed_date
