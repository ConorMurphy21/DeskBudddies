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
    #  tests date string format with 2 test dates to ensure sufficient data is kept from parsing
    date1 = datetime.datetime(2018, 11, 7)
    date2 = datetime.datetime(2019, 4, 1)
    result = _date_test(date1, format_str)
    result2 = _date_test(date2, format_str)
    if result == 0 or result2 == 0:
        return False
    else:
        return True


def _date_test(test_datetime: datetime, format_str: str) -> int:
    #  tests if data is lost between conversion of datetime to str and back
    #  return 1 if false date format, 2 if only day, 4 if day month, 6 if day,month,year
    year = test_datetime.year
    month = test_datetime.month
    day = test_datetime.day
    date1_str = test_datetime.strftime(format_str)
    test_datetime_new = test_datetime.strptime(date1_str, format_str)
    year_new = test_datetime_new.year
    month_new = test_datetime_new.month
    day_new = test_datetime_new.day

    if day != day_new:
        return 0
    if year != year_new or year < 2000:
        if month != month_new:
            return 1
        else:
            return 2
    elif month == month_new:
        return 3
    else:
        return 0


def _format_type(date_format: str) -> int:
    expected1 = datetime.datetime(2000, 2, 2)
    expected2 = datetime.datetime(2001, 3, 3)
    actual1 = datetime.datetime.strptime(expected1.strftime(date_format), date_format)
    actual2 = datetime.datetime.strptime(expected2.strftime(date_format), date_format)
    has_year = actual1.year == expected1.year and actual2.year == expected2.year
    has_month = actual1.month == expected1.month and actual2.month == expected2.month
    has_day = actual1.day == expected1.day and actual2.day == expected2.day
    if has_year and has_month and has_day:
        return 3
    elif has_month and has_day:
        return 2
    elif has_day:
        return 1
    else:
        return 0

def parse_date_str(date_str: str, format_str: str) -> datetime:
    #  assuming format_str has been checked with validate function
    true_date = datetime.datetime.now()
    tomorrow_datetime = datetime.datetime(true_date.year, true_date.month, true_date.day + 1)
    true_date = datetime.datetime(true_date.year, true_date.month, true_date.day)
    parsed_date = datetime.datetime.strptime(date_str, format_str)
    type_date_format = _format_type(format_str)
    if type_date_format == 0:
        raise ValueError("Unable to parse from improper date format")
    if type_date_format == 1:  # only day is given
        parsed_date_zeroed = datetime.datetime(true_date.year, true_date.month, parsed_date.day)
        if parsed_date_zeroed < true_date:
            parsed_date_zeroed = parsed_date_zeroed.replace(month=parsed_date_zeroed.month+1)
        fixed_parsed_date = datetime.datetime(parsed_date_zeroed.year, parsed_date_zeroed.month, parsed_date_zeroed.day)
    if type_date_format == 2:  # only day month is given
        parsed_date = parsed_date.replace(year=true_date.year)
        if parsed_date < true_date:
            # if greater then go back one year
            parsed_date = parsed_date.replace(year=tomorrow_datetime.year + 1)
            fixed_parsed_date = datetime.datetime(parsed_date.year, parsed_date.month, parsed_date.day)
        else:
            fixed_parsed_date = datetime.datetime(parsed_date.year, parsed_date.month, parsed_date.day)
    if type_date_format == 3:
        fixed_parsed_date = datetime.datetime(parsed_date.year, parsed_date.month, parsed_date.day)

    if fixed_parsed_date < true_date:
       raise ValueError()
    return fixed_parsed_date

