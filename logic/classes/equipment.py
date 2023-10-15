import json
from logic.classes.gadget import Gadget


class Equipment (object):
    """
    A class that represents an Equipment (a list of gadgets)
    """

    def __init__(self,
                 gadgets=None) -> object:
        """
        Constructor of the class
        :param gadgets: the list of gadgets
        :type gadgets: list
        """
        if gadgets is None:
            self.__gadgets = []
        else:
            self.__gadgets = gadgets

    @property
    def gadgets(self) -> list:
        """
        Getter for the list of gadgets
        :return: the list of gadgets
        :rtype: list
        """
        return self.__gadgets
    
    @gadgets.setter
    def gadgets(self, gadgets: list) -> None:
        """
        Setter for the list of gadgets
        :param gadgets: the new list of gadgets
        :type gadgets: list
        :return: None
        """
        self.__gadgets = gadgets

    def add_gadget(self, gadget: Gadget) -> None:
        """
        Adds a gadget to the list of gadgets
        :param gadget: the gadget to add
        :type gadget: Gadget
        :return: None
        """
        self.gadgets.append(gadget)

    def remove_gadget(self, gadget: Gadget) -> None:
        """
        Removes a gadget from the list of gadgets
        :param gadget: the gadget to remove
        :type gadget: Gadget
        :return: None
        """
        self.gadgets.remove(gadget)

    def __str__(self) -> str:
        """
        Returns the string representation of an Equipment
        :return: the string representation of an Equipment
        :rtype: str
        """
        gadgets_str = ""
        for gadget in self.gadgets:
            gadgets_str += gadget.__str__() + "\n"
        return gadgets_str
    
    def __eq__(self, other) -> bool:
        """
        Checks if two Equipment objects are equal
        :param other: the other Equipment object
        :type other: Equipment
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Equipment):
            return self.gadgets == other.gadgets
        return False


if __name__ == '__main__':
    gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
    gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
    gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')

    equipment = Equipment([gadget1, gadget2, gadget3])

    print(equipment)

    equipment.remove_gadget(gadget2)

    print(equipment)
