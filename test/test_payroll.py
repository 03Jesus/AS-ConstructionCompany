import unittest
from logic.classes.employee import Employee
from logic.classes.payroll import Payroll


class TestPayroll(unittest.TestCase):

    def test_constructor(self):

        employees = [Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor"),
                     Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")]
        payroll = Payroll(employees)
        self.assertEqual(payroll.employees, employees)

    def test_add_employee(self):

        payroll = Payroll()
        em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
        payroll.add_employee(em1)
        self.assertEqual(payroll.employees, [em1])

    def test_remove_employee(self):

        em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
        em2 = Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")
        payroll = Payroll([em1, em2])
        payroll.remove_employee(em1)
        self.assertEqual(payroll.employees, [em2])

    def __str__(self) -> str:

        employees_str = "\n".join(str(employee) for employee in self.employees)
        return f"Payroll(employees=[\n{employees_str}])"

    def test_eq(self):

        em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
        em2 = Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")
        em3 = Employee(3, "Maria", "Lopez", "12345678", "maria@lopez.com", "constructor")

        payroll1 = Payroll([em1, em2, em3])
        payroll2 = Payroll([em1, em2, em3])

        self.assertEqual(payroll1, payroll2)


if __name__ == '__main__':
    unittest.main()
