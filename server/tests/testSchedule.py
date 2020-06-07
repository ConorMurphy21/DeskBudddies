import os
import unittest
from datetime import datetime

from server.schedule import Schedule
from pathlib import Path


class TestSchedule(unittest.TestCase):

    date1 = datetime(2000, 5, 5)
    date2 = datetime(2000, 5, 6)
    date3 = datetime(2000, 6, 6)

    dates = [date1, date2, date3]

    def setUp(self) -> None:
        self.dir = Path.home() / Path('temp')
        self.schedule = Schedule(self.dir)

    def tearDown(self) -> None:
        os.remove(self.dir)

    def test_add_success(self):

        schedule = self.schedule

        pairs = {self.date1: ['Jen', 'Conor'],
                 self.date2: ['Jen'],
                 self.date3: ['Aliyah']}

        for (date, uids) in pairs.items():
            for uid in uids:
                schedule.add(uid, date)

        for (date, uids) in pairs.items():
            actual = schedule.get(date)
            expected = uids
            self.assertListEqual(actual, expected)

    def test_add_success_uncached(self):
        schedule = self.schedule

        pairs = {self.date1: ['Jen', 'Conor'],
                 self.date2: ['Jen'],
                 self.date3: ['Aliyah']}

        for (date, uids) in pairs.items():
            for uid in uids:
                schedule.add(uid, date)

        # remove the memory record of the schedule
        schedule.mem_sched = {}

        for (date, uids) in pairs:
            actual = schedule.get(date)
            expected = uids
            self.assertListEqual(actual, expected)

    def test_double_add(self):
        schedule = self.schedule
        success = schedule.add('Jen', self.date1)
        self.assertTrue(success)
        success = schedule.add('Jen', self.date1)
        self.assertFalse(success)
        actual = schedule.get(self.date1)
        expected = ['Jen']
        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
