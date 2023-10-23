import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.classes.employee import Employee
from logic.classes.payroll import Payroll


class TestPayroll(unittest.TestCase):

    def setUp(self):
        self.em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
        self.em2 = Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")
        self.em3 = Employee(3, "Maria", "Lopez", "12345678", "maria@lopez.com", "constructor")

    def test_constructor(self):
        employees = [self.em1, self.em2]
        payroll = Payroll(1, "PA1", employees)
        self.assertEqual(payroll.employees, employees)

    def test_add_employee(self):
        payroll = Payroll()
        payroll.add_child(self.em1)
        self.assertEqual(payroll.employees, [self.em1])

    def test_remove_employee(self):

        payroll = Payroll(2, "PA2", [self.em1, self.em2])
        payroll.remove_child(self.em1)
        self.assertEqual(payroll.employees, [self.em2])

    def __str__(self) -> str:
        employees_str = "\n".join(str(employee) for employee in self.employees)
        return f"Payroll(employees=[\n{employees_str}])"

    def test_eq(self):

        payroll1 = Payroll([self.em1, self.em2, self.em3])
        payroll2 = Payroll([self.em1, self.em2, self.em3])

        self.assertEqual(payroll1, payroll2)


if __name__ == '__main__':
    unittest.main()
