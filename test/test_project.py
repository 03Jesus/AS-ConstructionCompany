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

    def test_constructor(self):

        client = Client(1,
                        "Jesu",
                        "last_name",
                        "phone",
                        "mail")

        gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
        gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')

        equipment = Equipment([gadget1, gadget2, gadget3])

        schedule = Schedule(1,
                            "start_date",
                            "finish_date",
                            "state")

        em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
        em2 = Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")

        payroll = Payroll([em1, em2])
        
        children = [client, equipment, schedule, payroll]

        project = Project(1,
                          "Construction House",
                          "description",
                          children)

        self.assertEqual(project.id, 1)
        self.assertEqual(project.name, "Construction House")
        self.assertEqual(project.description, "description")
        self.assertEqual(project.children, children)

    def test_eq(self):

        client = Client(1,
                        "Jesu",
                        "last_name",
                        "phone",
                        "mail")

        gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
        gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')

        equipment = Equipment([gadget1, gadget2, gadget3])

        schedule = Schedule(1,
                            "start_date",
                            "finish_date",
                            "state")

        em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
        em2 = Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")

        payroll = Payroll([em1, em2])
        
        children = [client, equipment, schedule, payroll]

        project1 = Project(1,
                           "Construction House",
                           "description",
                           children)

        project2 = Project(1,
                           "Construction House",
                           "description",
                           children)

        self.assertEqual(project1, project2)


if __name__ == '__main__':
    unittest.main()