import unittest
import datetime as dt

from cmnUtils import dateUtils as util


class MyTestCase(unittest.TestCase):
    def test_get_week(self):
        monday = util.get_next_weekday(0)
        # make sure to zero time
        monday = dt.datetime(monday.year, monday.month, monday.day)
        for i in range(52):
            day = dt.datetime(monday.year, monday.month, monday.day)

            for i in range(6):
                firstday = util.get_week(monday, True)
                expected = monday.strftime("%Y%m%d")
                actual = firstday.strftime("%Y%m%d")
                self.assertEqual(actual, expected)
                day = day + dt.timedelta(days=1)
            monday = monday + dt.timedelta(weeks=1)


if __name__ == '__main__':
    unittest.main()
