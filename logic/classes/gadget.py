import json
from logic.classes.component import Component


class Gadget (Component):
    """
    A class that represents an Gadget
    """

    def __init__(self,
                 id: int = 0,
                 name: str = 'name',
                 type: str = "type",
                 state: str = 'state',) -> object:
        """
        Constructor of the class
        :param id: the id of the Gadget
        :type id: int
        :param name: the name of the Gadget
        :type name: str
        :param state: the state of the Gadget
        :type state: str
        """
        self.__id = id
        self.__name = name
        self.__type = type
        self.__state = state

    @property
    def id(self) -> int:
        """
        Getter for the id of the Gadget
        :return: the id of the Gadget
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Gadget
        :param id: the new id of the Gadget
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def name(self) -> str:
        """
        Getter for the name of the Gadget
        :return: the name of the Gadget
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for the name of the Gadget
        :param name: the new name of the Gadget
        :type name: str
        :return: None
        """
        self.__name = name

    @property
    def state(self) -> str:
        """
        Getter for the state of the Gadget
        :return: the state of the Gadget
        :rtype: str
        """
        return self.__state

    @state.setter
    def state(self, state: str) -> None:
        """
        Setter for the state of the Gadget
        :param state: the new state of the Gadget
        :type state: str
        :return: None
        """
        self.__state = state

    @property
    def type(self) -> str:
        """
        Getter for the state of the Gadget
        :return: the state of the Gadget
        :rtype: str
        """
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        """
        Setter for the state of the Gadget
        :param state: the new state of the Gadget
        :type state: str
        :return: None
        """
        self.__type = type

    def get_name(self) -> str:
        return self.name

    def show_details(self, depth: int) -> None:
        prefix = "  " * depth
        print(
            f"{prefix}Gadget(id={self.id}, name='{self.name}', type='{self.type}' state='{self.state}')")

    def __str__(self) -> str:
        """
        Returns the string representation of an Gadget
        :return: the string representation of an Gadget
        :rtype: str
        """
        return f"Gadget(id={self.id}, name='{self.name}', type='{self.type}' state='{self.state}')"

    def __eq__(self, other) -> bool:
        """
        Returns True if the Gadgets are equal, False otherwise
        :param other: the other Gadget
        :type other: object
        :return: True if the Gadgets are equal, False otherwise
        :rtype: bool
        """
        return self.id == other.id and \
            self.name == other.name and \
            self.state == other.state \
            and self.type == other.type


if __name__ == '__main__':
    gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
    gadget2 = Gadget(2, 'gadget2', 'type1', 'state2')
    gadget3 = Gadget(3, 'gadget3', 'type1', 'state3')

    assert gadget1.id == 1

    if gadget1 == gadget2:
        print('gadget1 == gadget2')
    else:
        print('gadget1 != gadget2')
