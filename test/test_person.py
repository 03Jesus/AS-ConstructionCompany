from logic.classes.person import Person
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

JHON_DOE_MAIL = 'johndoe@example.com'
ALICE_JOHNSON_MAIL = 'alice@example.com'


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person1 = Person(1, 'John', 'Doe', '1234567890', JHON_DOE_MAIL)
        self.person2 = Person(2, 'Alice', 'Johnson',
                              '9876543210', ALICE_JOHNSON_MAIL)
        self.person3 = Person(1, 'John', 'Doe', '1234567890', JHON_DOE_MAIL)

    def test_instance(self):
        self.assertIsInstance(self.person1, Person,
                              "It's an instance of Person!")

    def test_id(self):
        self.assertEqual(self.person1.id, 1)

    def test_name(self):
        self.assertEqual(self.person1.name, 'John')

    def test_last_name(self):
        self.assertEqual(self.person1.last_name, 'Doe')

    def test_phone(self):
        self.assertEqual(self.person1.phone, '1234567890')

    def test_mail(self):
        self.assertEqual(self.person1.mail, JHON_DOE_MAIL)

    def test_setters(self):
        self.person1.id = 2
        self.person1.name = 'Alice'
        self.person1.last_name = 'Johnson'
        self.person1.phone = '9876543210'
        self.person1.mail = 'alice@example.com'
        self.assertEqual(self.person1.id, 2)
        self.assertEqual(self.person1.name, 'Alice')
        self.assertEqual(self.person1.last_name, 'Johnson')
        self.assertEqual(self.person1.phone, '9876543210')
        self.assertEqual(self.person1.mail, ALICE_JOHNSON_MAIL)

    def test_str_representation(self):
        expected_str = "Person(id=1, name='John', last_name='Doe', phone='1234567890', mail='johndoe@example.com')"
        self.assertEqual(str(self.person1), expected_str)

    def test_equality(self):
        self.assertEqual(self.person1, self.person3)
        self.assertNotEqual(self.person1, self.person2)


if __name__ == '__main__':
    unittest.main()
