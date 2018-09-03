import unittest
import datetime
from src.datecalculation import next_draw_date, WED, SAT
from src.datecalculation2 import next_draw_date as next_draw_date2


class TestDateCalculation(unittest.TestCase):

    def test_sameday(self):
        _date = datetime.datetime(2018, 8, 22, 11, 0)
        d = next_draw_date(_date)
        self.assertEqual(d.weekday(), _date.weekday())

        d2 = next_draw_date2(_date)
        self.assertEqual(d, d2)

        _date = datetime.datetime(2018, 8, 25, 19, 0)
        d = next_draw_date(_date)
        self.assertEqual(d.weekday(), _date.weekday())

        d2 = next_draw_date2(_date)
        self.assertEqual(d, d2)

    def test_next_wednesday(self):
        _date = datetime.datetime(2018, 8, 21, 11, 0)
        d = next_draw_date(_date)
        self.assertEqual(d, datetime.datetime(2018, 8, 22, 20, 0, 0, 0))
        self.assertEqual(d.weekday(), WED)

        d2 = next_draw_date2(_date)
        self.assertEqual(d, d2)

        _date = datetime.datetime(2018, 8, 26, 11, 0)
        d = next_draw_date(_date)
        self.assertEqual(d, datetime.datetime(2018, 8, 29, 20, 0, 0, 0))
        self.assertEqual(d.weekday(), WED)
        d2 = next_draw_date2(_date)
        self.assertEqual(d, d2)

    def test_next_saturday(self):
        _date = datetime.datetime(2018, 8, 22, 20, 0)
        d = next_draw_date(_date)
        self.assertEqual(d, datetime.datetime(2018, 8, 25, 20, 0, 0, 0))
        self.assertEqual(d.weekday(), SAT)

        d2 = next_draw_date2(_date)
        self.assertEqual(d, d2)

        _date = datetime.datetime(2018, 9, 5, 20, 0)
        d = next_draw_date(_date)
        self.assertEqual(d, datetime.datetime(2018, 9, 8, 20, 0, 0, 0))
        self.assertEqual(d.weekday(), SAT)

        d2 = next_draw_date2(_date)
        self.assertEqual(d, d2)

    def test_default(self):
        d = next_draw_date()
        self.assertIn(d.weekday(), [SAT, WED])

        d2 = next_draw_date2()
        self.assertEqual(d, d2)
