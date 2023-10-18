import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.classes.schedule import Schedule
from datetime import date


class TestSchedule(unittest.TestCase):

    def test_constructor(self):

        today = date.today()
        schedule = Schedule(1, today, today, 'state')

        self.assertEqual(schedule.id, 1)
        self.assertEqual(schedule.start_date, today)
        self.assertEqual(schedule.finish_date, today)
        self.assertEqual(schedule.state, 'state')

    def test_str(self):

        today = date.today()
        schedule = Schedule(1, today, today, 'state')

        expected_str = f"Schedule(id=1, start_date='{today}', finish_date='{today}', state='state')"

        self.assertEqual(str(schedule), expected_str)

    def test_eq(self):

        today = date.today()
        schedule1 = Schedule(1, today, today, 'state')
        schedule2 = Schedule(1, today, today, 'state')
        schedule3 = Schedule(2, today, today, 'state')
        schedule4 = Schedule(1, today, today, 'state2')

        self.assertEqual(schedule1, schedule2)
        self.assertNotEqual(schedule1, schedule3)
        self.assertNotEqual(schedule1, schedule4)


if __name__ == '__main__':
    unittest.main()
