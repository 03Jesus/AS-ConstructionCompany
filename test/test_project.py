import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.classes.project import Project
from logic.classes.client import Client
from logic.classes.equipment import Equipment
from logic.classes.schedule import Schedule
from logic.classes.payroll import Payroll
from logic.classes.employee import Employee
from logic.classes.gadget import Gadget


class TestProject(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Jesus", "last_name", "phone", "mail")
        self.gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        self.gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
        self.gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')
        self.equipment = Equipment([self.gadget1, self.gadget2, self.gadget3])
        self.schedule = Schedule(1, "start_date", "finish_date", "state")
        self.em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
        self.em2 = Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")
        self.payroll = Payroll([self.em1, self.em2])

        self.children = [self.client, self.equipment, self.schedule, self.payroll]

        self.project1 = Project(1, "Construction House", "description", self.children)

        self.project2 = Project(1, "Construction House", "description", self.children)

    def test_constructor(self):

        self.assertEqual(self.project1.id, 1)
        self.assertEqual(self.project1.name, "Construction House")
        self.assertEqual(self.project1.description, "description")
        self.assertEqual(self.project1.children, self.children)

    def test_eq(self):

        self.assertEqual(self.project1, self.project2)


if __name__ == '__main__':
    unittest.main()
