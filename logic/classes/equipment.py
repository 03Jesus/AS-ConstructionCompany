from typing import List

from logic.classes.component import Component
from logic.classes.list_component import ListComponent
from logic.classes.gadget import Gadget


class Equipment (ListComponent):
    """
    A class that represents an Equipment (A list of gadgets)
    """

    def __init__(self,
                 id: int = 0,
                 name: str = "name",
                 gadgets: List[Gadget] = None) -> ListComponent:
        """
        Constructor for the Equipment class
        :param id: the id of the Equipment
        :type id: int
        :param gadgets: the list of gadgets of the Equipment
        :type gadgets: List[Gadget]
        """
        self.__id = id
        self.__name = name
        if gadgets is None:
            self.__gadgets = []
        else:
            self.__gadgets = gadgets

    @property
    def id(self) -> int:
        """
        Getter for the id of the Equipment
        :return: the id of the Equipment
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Equipment
        :param id: the new id of the Equipment
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def name(self) -> str:
        """
        Getter for the name of the Equipment
        :return: the name of the Equipment
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for the name of the Equipment
        :param name: the new name of the Equipment
        :type name: str
        :return: None
        """
        self.__name = name

    @property
    def gadgets(self) -> List[Gadget]:
        """
        Getter for the gadgets of the Equipment
        :return: the gadgets of the Equipment
        :rtype: List[Gadget]
        """
        return self.__gadgets

    @gadgets.setter
    def gadgets(self, gadgets: List[Gadget]) -> None:
        """
        Setter for the gadgets of the Equipment
        :param gadgets: the new gadgets of the Equipment
        :type gadgets: List[Gadget]
        :return: None
        """
        self.__gadgets = gadgets

    def add_child(self, child: Gadget) -> None:
        """
        Adds a new gadget to the Equipment
        :param child: the new gadget
        :type child: Gadget
        :return: None
        """
        self.__gadgets.append(child)

    def remove_child(self, child: Gadget) -> None:
        """
        Removes a gadget from the Equipment
        :param child: the gadget to remove
        :type child: Gadget
        :return: None
        """
        self.__gadgets.remove(child)

    def get_name(self) -> str:
        return self.name

    def show_details(self, depth: int) -> None:
        prefix = "  " * depth
        print(f"{prefix}Equipment: {self.name}")
        for gadget in self.gadgets:
            gadget.show_details(depth + 1)

    def __str__(self) -> str:
        """
        Returns the string representation of an Equipment
        :return: the string representation of an Equipment
        :rtype: str
        """
        return f"Equipment(id={self.id}, name='{self.name}', gadgets={self.gadgets})"

    def __eq__(self, other: object) -> bool:
        """
        Compares two Equipment objects
        :param other: the other Equipment object
        :type other: object
        :return: True if both Equipment objects are the same, False otherwise
        :rtype: bool
        """
        if isinstance(other, Equipment):
            return self.id == other.id and self.name == other.name and self.gadgets == other.gadgets
        return False


if __name__ == "__main__":

    gadget1 = Gadget(1, 'Hammer', 'Hand Tool', 'Available')
    gadget2 = Gadget(2, 'Screwdriver', 'Hand Tool', 'Available')
    gadget3 = Gadget(3, 'Drill', 'Power Tool', 'Available')

    equipment = Equipment(1, "equipment 1", [gadget1, gadget2])
    equipment.show_details(0)
