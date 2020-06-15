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
    result = _date_test(date1, format_str) + _date_test(date2, format_str)
    if result % 2 == 0:
        return True
    else:
        print("Date format doesn't keep track of day")
        return False


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
        return 1
    if year != year_new:
        if month != month_new:
            return 2
        else:
            return 4
    elif month == month_new:
        return 6
    else:
        return 1


def parse_date_str(date_str: str, format_str: str) -> datetime:
    #  assuming format_str has been checked with validate function
    parsed_date = datetime.datetime.strptime(date_str, format_str)
    tomorrow_datetime = datetime.datetime.now()
    current_day = datetime.date(tomorrow_datetime.year,tomorrow_datetime.month,tomorrow_datetime.day)
    #   move it back one day
    tomorrow_datetime = datetime.date(tomorrow_datetime.year, tomorrow_datetime.month, tomorrow_datetime.day - 1)
    type_date_format = _date_test(parsed_date, format_str)

    if type_date_format == 2:  # only day is given
        parsed_date_zeroed = datetime.date(parsed_date)
        days_to_add = abs(current_day.day - parsed_date_zeroed().day)
        if parsed_date_zeroed == current_day:
            fixed_parsed_date = datetime.datetime(parsed_date.year, parsed_date.month, parsed_date.day)
        elif parsed_date_zeroed > current_day:
            fixed_parsed_date = current_day + current_day.timedelta(days=days_to_add)
        else:
            fixed_parsed_date = current_day - current_day.timedelta(days=days_to_add)
    if type_date_format == 4:  # only day month is given
        parsed_date = parsed_date.date().replace(year=current_day.year)
        if parsed_date >= current_day:
            # if greater then go back one year
            parsed_date = parsed_date.replace(year=tomorrow_datetime.year - 1)
            fixed_parsed_date = datetime.datetime(parsed_date.year, parsed_date.month, parsed_date.day)
    else:
        fixed_parsed_date = datetime.datetime(parsed_date.year, parsed_date.month, parsed_date.day)
    if parsed_date < datetime.datetime.now():
        print("day has already passed")
        #throw error
    return fixed_parsed_date
