import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.classes.equipment import Equipment
from logic.classes.gadget import Gadget


class TestEquipment(unittest.TestCase):

    def test_constructor(self):

        gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
        gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')

        equipment = Equipment(1, "EQ1", [gadget1, gadget2, gadget3])

        self.assertEqual(equipment.gadgets, [gadget1, gadget2, gadget3])

    def test_add_gadget(self):

        gadget = Gadget(4, 'gadget4', 'type4', 'state4')

        equipment = Equipment()

        equipment.add_child(gadget)

        self.assertEqual(equipment.gadgets, [gadget])

    def test_remove_gadget(self):

        gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
        gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')

        equipment = Equipment(2, "EQ2", [gadget1, gadget2, gadget3])

        equipment.remove_child(gadget2)

        self.assertEqual(equipment.gadgets, [gadget1, gadget3])


if __name__ == '__main__':
    unittest.main()
