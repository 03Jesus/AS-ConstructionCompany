import unittest
from logic.classes.gadget import Gadget


class TestGadget(unittest.TestCase):

    def test_constructor(self):

        gadget = Gadget(1, 'gadget1', 'type1', 'state1')

        self.assertEqual(gadget.id, 1)
        self.assertEqual(gadget.name, 'gadget1')
        self.assertEqual(gadget.type, 'type1')
        self.assertEqual(gadget.state, 'state1')

    def test_str(self):

        gadget = Gadget(1, 'gadget1', 'type1', 'state1')

        expected_str = f"Gadget(id=1, name='gadget1', type='type1' state='state1')"

        self.assertEqual(str(gadget), expected_str)

    def test_eq(self):

        gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        gadget2 = Gadget(1, 'gadget1', 'type1', 'state1')
        gadget3 = Gadget(2, 'gadget2', 'type2', 'state2')

        self.assertEqual(gadget1, gadget2)
        self.assertNotEqual(gadget1, gadget3)


if __name__ == '__main__':
    unittest.main()
