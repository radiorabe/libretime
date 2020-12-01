import datetime
import unittest
from api_clients import utils

class TestTime(unittest.TestCase):
    def test_time_in_seconds(self):
        time = datetime.time(hour=0, minute=3, second=34, microsecond=649600)
        self.assertTrue(abs(utils.time_in_seconds(time) - 214.65) < 0.009)

    def test_time_in_milliseconds(self):
        time = datetime.time(hour=0, minute=0, second=0, microsecond=500000)
        self.assertEqual(utils.time_in_milliseconds(time), 500)

if __name__ == '__main__': unittest.main()
