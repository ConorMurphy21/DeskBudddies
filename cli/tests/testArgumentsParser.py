import unittest

from cli import argsParser


class MyTestCase(unittest.TestCase):

    def test_parse_and_validate_day(self):
        days = ['Mon', 'FRIDAY', 'wed', 'thurs', 'tues', 'tue', 'Saturday', 'sun']
        expected = [0, 4, 2, 3, 1, 1, 5, 6]
        args = ArgsModel()
        args.query = True

        for day in days:
            args.day = day
            success = argsParser._parse_and_validate(args)
            self.assertTrue(success)

            actual_day = args.day
            expected_day = expected[days.index(day)]
            self.assertEqual(actual_day, expected_day)

    # will test later that the date is actually right (when it actually works, for now just test that it doesn't break)
    def test_parse_and_validate_date(self):
        args = ArgsModel()
        args.date = '01/01'
        success = argsParser._parse_and_validate(args)
        self.assertTrue(success)

    def test_parse_and_validate_default_action(self):
        args = ArgsModel()
        args.day = 'Mon'
        success = argsParser._parse_and_validate(args)
        self.assertTrue(success)

    def test_double_action_fail(self):
        args = ArgsModel()
        args.config = True
        args.serve = True
        args.day = 'Mon'
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)
        args = ArgsModel()
        args.query = True
        args.remove = True
        args.day = 'Mon'
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)
        args = ArgsModel()
        args.get = True
        args.remove = True
        args.day = 'Mon'
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)

    def test_double_date_fail(self):
        args = ArgsModel()
        args.day = 'Tues'
        args.date = '01/01'
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)

    def test_date_required_fail(self):
        args = ArgsModel()
        args.query = True
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)
        args = ArgsModel()
        args.remove = True
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)
        args = ArgsModel()
        args.get = True
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)

    def test_no_date_required(self):
        args = ArgsModel()
        args.config = True
        success = argsParser._parse_and_validate(args)
        self.assertTrue(success)
        args = ArgsModel()
        args.serve = True
        success = argsParser._parse_and_validate(args)
        self.assertTrue(success)

    def test_date_fail(self):
        args = ArgsModel()
        args.date = 'asdf'
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)

    def test_day_fail(self):
        args = ArgsModel()
        args.day = 'asdflkjasdf'
        success = argsParser._parse_and_validate(args)
        self.assertFalse(success)


class ArgsModel:

    def __init__(self):
        self.serve = False
        self.query = False
        self.remove = False
        self.get = False
        self.config = False
        self.action = None
        self.day = None
        self.date = None

if __name__ == '__main__':
    unittest.main()
