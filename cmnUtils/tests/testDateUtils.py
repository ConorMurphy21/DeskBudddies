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


if __name__ == '__main__':
    unittest.main()
