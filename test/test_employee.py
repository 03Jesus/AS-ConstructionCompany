import unittest
from logic.classes.employee import Employee


class TestEmployee(unittest.TestCase):

    def test_constructor(self):

        employee = Employee(1, 'name', 'last_name', 'phone', 'mail', 'type')

        self.assertEqual(employee.id, 1)
        self.assertEqual(employee.name, 'name')
        self.assertEqual(employee.last_name, 'last_name')
        self.assertEqual(employee.phone, 'phone')
        self.assertEqual(employee.mail, 'mail')
        self.assertEqual(employee.type, 'type')

    def test_type_getter_and_setter(self):

        employee = Employee(1, 'name', 'last_name', 'phone', 'mail', 'type')

        self.assertEqual(employee.type, 'type')

        employee.type = 'new_type'

        self.assertEqual(employee.type, 'new_type')

    def test_str(self):

        employee = Employee(1, 'name', 'last_name', 'phone', 'mail', 'type')

        expected_str = f"Employee(id={1}, name='name', last_name='last_name', phone='phone', mail='mail', type='type')"

        self.assertEqual(employee.__str__(), expected_str)

    def test_eq(self):

        employee1 = Employee(1, 'name', 'last_name', 'phone', 'mail', 'type')
        employee2 = Employee(1, 'name', 'last_name', 'phone', 'mail', 'type')
        employee3 = Employee(2, 'name2', 'last_name2', 'phone2', 'mail2', 'type2')

        self.assertEqual(employee1, employee2)
        self.assertNotEqual(employee1, employee3)


if __name__ == '__main__':
    unittest.main()
