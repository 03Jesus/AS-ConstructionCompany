import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.classes.gadget import Gadget


class TestGadget(unittest.TestCase):

    def setUp(self):
        self.gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
        self.gadget2 = Gadget(1, 'gadget1', 'type1', 'state1')
        self.gadget3 = Gadget(2, 'gadget2', 'type2', 'state2')

    def test_constructor(self):

        self.assertEqual(self.gadget1.id, 1)
        self.assertEqual(self.gadget1.name, 'gadget1')
        self.assertEqual(self.gadget1.type, 'type1')
        self.assertEqual(self.gadget1.state, 'state1')

    def test_str(self):

        expected_str = "Gadget(id=1, name='gadget1', type='type1' state='state1')"

        self.assertEqual(str(self.gadget1), expected_str)

    def test_eq(self):

        self.assertEqual(self.gadget1, self.gadget2)
        self.assertNotEqual(self.gadget1, self.gadget3)


if __name__ == '__main__':
    unittest.main()
