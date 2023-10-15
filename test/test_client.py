import unittest
from logic.classes.client import Client


class TestClient(unittest.TestCase):

    def test_constructor(self):

        client = Client(1, 'name', 'last_name', 'phone', 'mail')

        self.assertEqual(client.id, 1)
        self.assertEqual(client.name, 'name')
        self.assertEqual(client.last_name, 'last_name')
        self.assertEqual(client.phone, 'phone')
        self.assertEqual(client.mail, 'mail')

    def test_str(self):

        client = Client(1, 'name', 'last_name', 'phone', 'mail')

        expected_str = f"Client(id=1, name='name', last_name='last_name', phone='phone', mail='mail')"

        self.assertEqual(client.__str__(), expected_str)

    def test_eq(self):

        client1 = Client(1, 'name', 'last_name', 'phone', 'mail')
        client2 = Client(1, 'name', 'last_name', 'phone', 'mail')
        client3 = Client(2, 'name2', 'last_name2', 'phone2', 'mail2')

        self.assertEqual(client1, client2)
        self.assertNotEqual(client1, client3)


if __name__ == '__main__':
    unittest.main()
