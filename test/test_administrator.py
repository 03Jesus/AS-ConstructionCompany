import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.classes.administrator import Administrator

class TestAdministrator(unittest.TestCase):

    def test_constructor(self):

        administrator = Administrator(1, 'name', 'last_name', 'phone', 'mail')

        self.assertEqual(administrator.id, 1)
        self.assertEqual(administrator.name, 'name')
        self.assertEqual(administrator.last_name, 'last_name')
        self.assertEqual(administrator.phone, 'phone')
        self.assertEqual(administrator.mail, 'mail')

    def test_str(self):

        administrator = Administrator(1, 'name', 'last_name', 'phone', 'mail')

        expected_str = f"Administrator: 1, name, last_name, phone, mail"

        self.assertEqual(administrator.__str__(), expected_str)

    def test_eq(self):

        administrator1 = Administrator(1, 'name', 'last_name', 'phone', 'mail')
        administrator2 = Administrator(1, 'name', 'last_name', 'phone', 'mail')
        administrator3 = Administrator(
            2, 'name2', 'last_name2', 'phone2', 'mail2')

        self.assertEqual(administrator1, administrator2)
        self.assertNotEqual(administrator1, administrator3)


if __name__ == '__main__':
    unittest.main()
