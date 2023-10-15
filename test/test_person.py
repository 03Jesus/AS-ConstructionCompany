import unittest
from logic.classes.person import Person


class TestPerson(unittest.TestCase):
    def test_instance(self):
        person = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        self.assertIsInstance(person, Person, "It's an instance of Person!")

    def test_id(self):
        person = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        self.assertEqual(person.id, 1)

    def test_name(self):
        person = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        self.assertEqual(person.name, 'John')

    def test_last_name(self):
        person = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        self.assertEqual(person.last_name, 'Doe')

    def test_phone(self):
        person = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        self.assertEqual(person.phone, '1234567890')

    def test_mail(self):
        person = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        self.assertEqual(person.mail, 'johndoe@example.com')

    def test_setters(self):
        person = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        person.id = 2
        person.name = 'Alice'
        person.last_name = 'Johnson'
        person.phone = '9876543210'
        person.mail = 'alice@example.com'
        self.assertEqual(person.id, 2)
        self.assertEqual(person.name, 'Alice')
        self.assertEqual(person.last_name, 'Johnson')
        self.assertEqual(person.phone, '9876543210')
        self.assertEqual(person.mail, 'alice@example.com')

    def test_str_representation(self):
        person = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        expected_str = "Person(id=1, name='John', last_name='Doe', phone='1234567890', mail='johndoe@example.com')"
        self.assertEqual(str(person), expected_str)

    def test_equality(self):
        p1 = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        p2 = Person(2, 'Alice', 'Johnson', '9876543210', 'alice@example.com')
        p3 = Person(1, 'John', 'Doe', '1234567890', 'johndoe@example.com')
        self.assertEqual(p1, p3)  # p1 and p3 should be equal
        self.assertNotEqual(p1, p2)  # p1 and p2 should not be equal


if __name__ == '__main__':
    unittest.main()
