import unittest
import datetime as dt

from cmnUtils import dateUtils as util


class MyTestCase(unittest.TestCase):

    def test_get_week(self):
        monday = util.get_next_weekday(0)
        # make sure to zero time
        monday = dt.datetime(monday.year, monday.month, monday.day)
        self.simple_get_week_test(monday)

    def test_get_week_sunday(self):
        sunday = util.get_next_weekday(6)
        # make sure to zero time
        sunday = dt.datetime(sunday.year, sunday.month, sunday.day)
        self.simple_get_week_test(sunday)

    def simple_get_week_test(self, firstday: dt.datetime):
        monday_first = firstday.weekday() == 0
        for i in range(52):
            day = dt.datetime(firstday.year, firstday.month, firstday.day)

            for j in range(6):
                result = util.get_week(day, monday_first)
                expected = firstday.strftime("%Y%m%d")
                actual = result.strftime("%Y%m%d")
                self.assertEqual(actual, expected)
                self.assertEqual(firstday.weekday(), result.weekday())
                day = day + dt.timedelta(days=1)
            firstday = firstday + dt.timedelta(weeks=1)

    def test_validate_date_format_success(self):
        valid_formats = ['%d,%m,%Y', '%d/%b %H %I', '%d', '%B.%d %p', '%d/%m/%y']
        for date_format in valid_formats:
            self.assertTrue(util.validate_date_format(date_format))

    def test_validate_date_format_fail(self):
        invalid_formats = ['', '%m', '%m,%Y', '%d,%Y', '%b/%y/%I/%H']
        for date_format in invalid_formats:
            self.assertFalse(util.validate_date_format(date_format))

    def test_parse_date_past_date(self):
        date = dt.datetime(2019, 1, 1)
        date_str = date.strftime("%Y%m%d")
        self.assertRaises(ValueError, lambda: util.parse_date_str(date_str, "%Y%m%d"))

    def test_today_success(self):
        date = dt.date.today()
        date_str = date.strftime("%Y%m%d")
        result = util.parse_date_str(date_str, "%Y%m%d").strftime("%Y%m%d")
        self.assertEqual(date_str, result)

    def test_parse_date_just_day(self):
        # at least 1 of these should stay in the same month
        # at least 1 of these should go to the next
        date = dt.datetime.today()
        self.assert_date_parse_works(date, "%d")
        date = dt.datetime.today() + dt.timedelta(days=1)
        self.assert_date_parse_works(date, "%d")
        date = dt.datetime.today() + dt.timedelta(days=6)
        self.assert_date_parse_works(date, "%d")
        date = dt.datetime.today() + dt.timedelta(days=16)
        self.assert_date_parse_works(date, "%d")

    def test_parse_date_day_month(self):
        date = dt.datetime.today()
        self.assert_date_parse_works(date, "%d%m")
        date = dt.datetime.today() + dt.timedelta(days=40)
        self.assert_date_parse_works(date, "%d%m")
        date = dt.datetime.today() + dt.timedelta(days=364)
        self.assert_date_parse_works(date, "%d%m")

    def assert_date_parse_works(self, date: dt.datetime, date_format: str):
        date_str = date.strftime(date_format)
        actual = util.parse_date_str(date_str, date_format).strftime("%Y%m%d")
        expected = date.strftime("%Y%m%d")
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
