import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.classes.administrator import Administrator


class TestAdministrator(unittest.TestCase):

    def setUp(self):
        self.administrator1 = Administrator(1, 'name', 'last_name', 'phone', 'mail')
        self.administrator2 = Administrator(1, 'name', 'last_name', 'phone', 'mail')
        self.administrator3 = Administrator(2, 'name2', 'last_name2', 'phone2', 'mail2')

    def test_constructor(self):

        self.assertEqual(self.administrator1.id, 1)
        self.assertEqual(self.administrator1.name, 'name')
        self.assertEqual(self.administrator1.last_name, 'last_name')
        self.assertEqual(self.administrator1.phone, 'phone')
        self.assertEqual(self.administrator1.mail, 'mail')

    def test_str(self):

        expected_str = "Administrator: 1, name, last_name, phone, mail"

        self.assertEqual(self.administrator1.__str__(), expected_str)

    def test_eq(self):

        self.assertEqual(self.administrator1, self.administrator2)
        self.assertNotEqual(self.administrator1, self.administrator3)


if __name__ == '__main__':
    unittest.main()
