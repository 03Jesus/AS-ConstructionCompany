import unittest
from logic.classes.equipment import Equipment
from logic.classes.gadget import Gadget


class TestEquipment(unittest.TestCase):

    def test_constructor(self):

        gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
        gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')

        equipment = Equipment([gadget1, gadget2, gadget3])

        self.assertEqual(equipment.gadgets, [gadget1, gadget2, gadget3])

    def test_add_gadget(self):

        gadget = Gadget(4, 'gadget4', 'type4', 'state4')

        equipment = Equipment()

        equipment.add_gadget(gadget)

        self.assertEqual(equipment.gadgets, [gadget])

    def test_remove_gadget(self):

        gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
        gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')

        equipment = Equipment([gadget1, gadget2, gadget3])

        equipment.remove_gadget(gadget2)

        self.assertEqual(equipment.gadgets, [gadget1, gadget3])


if __name__ == '__main__':
    unittest.main()
