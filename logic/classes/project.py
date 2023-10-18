from datetime import date
from typing import List

from logic.classes.component import Component
from logic.classes.list_component import ListComponent
from logic.classes.client import Client
from logic.classes.equipment import Equipment
from logic.classes.schedule import Schedule
from logic.classes.payroll import Payroll
from logic.classes.employee import Employee
from logic.classes.gadget import Gadget


class Project (ListComponent):
    """
    A class that represents a Project
    """

    def __init__(self,
                 id: int = 0,
                 name: str = 'name',
                 description: str = 'description',
                 children: List[Component] = None) -> ListComponent:
        """
        Constructor for the Project class
        :param id: the id of the Project
        :type id: int
        :param name: the name of the Project
        :type name: str
        :param description: the description of the Project
        :type description: str
        :param children: the list of children of the Project
        :type children: List[Component]
        """
        self.__id = id
        self.__name = name
        self.__description = description
        if children is None:
            self.__children = []
        else:
            self.__children = children

    @property
    def id(self) -> int:
        """
        Getter for the id of the Project
        :return: the id of the Project
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Project
        :param id: the new id of the Project
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def name(self) -> str:
        """
        Getter for the name of the Project
        :return: the name of the Project
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for the name of the Project
        :param name: the new name of the Project
        :type name: str
        :return: None
        """
        self.__name = name

    @property
    def description(self) -> str:
        """
        Getter for the description of the Project
        :return: the description of the Project
        :rtype: str
        """
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        """
        Setter for the description of the Project
        :param description: the new description of the Project
        :type description: str
        :return: None
        """
        self.__description = description

    @property
    def children(self) -> List[Component]:
        """
        Getter for the children of the Project
        :return: the children of the Project
        :rtype: List[Component]
        """
        return self.__children

    @children.setter
    def children(self, children: List[Component]) -> None:
        """
        Setter for the children of the Project
        :param children: the new children of the Project
        :type children: List[Component]
        :return: None
        """
        self.__children = children

    def add_child(self, child: Component) -> None:
        """
        Method that adds a child to the Project
        :param child: the child to be added
        :type child: Component
        :return: None
        """
        self.children.append(child)

    def remove_child(self, child: Component) -> None:
        """
        Method that removes a child from the Project
        :param child: the child to be removed
        :type child: Component
        :return: None
        """
        self.children.remove(child)

    def get_name(self) -> str:
        return self.name

    def show_details(self, depth: int) -> None:
        """
        Method that prints the details of the Project
        :param depth: the depth of the Project in the tree
        :type depth: int
        :return: None
        """
        prefix = "  " * depth
        print(f"{prefix}Project: {self.name}")
        for child in self.children:
            child.show_details(depth + 1)

    def __str__(self) -> str:
        """
        String representation of the Project
        :return: a string containing the Project
        :rtype: str
        """
        return f"Project(id={self.id}, name='{self.name}', client={str(self.client)}, description='{self.description}', equipment={str(self.equipment.show_details())}, schedule={str(self.schedule)}, payroll={str(self.payroll.show_details())})"

    def __eq__(self, other: object) -> bool:
        """
        Method that checks if two Projects are equal
        :param other: the other Project
        :type other: object
        :return: True if the Projects are equal, False otherwise
        :rtype: bool
        """
        if not isinstance(other, Project):
            return False
        return self.__id == other.id and \
            self.__name == other.name and \
            self.__description == other.description and \
            self.__children == other.children


if __name__ == "__main__":

    client1 = Client(1, 'John', 'Doe', '1234567890', 'john.doe@example.com')
    client2 = Client(2, 'Jane', 'Smith', '9876543210',
                     'jane.smith@example.com')
    client3 = Client(3, 'Michael', 'Johnson', '5555555555',
                     'michael.johnson@example.com')

    gadget1 = Gadget(1, 'Hammer', 'Hand Tool', 'Available')
    gadget2 = Gadget(2, 'Screwdriver', 'Hand Tool', 'Available')
    gadget3 = Gadget(3, 'Drill', 'Power Tool', 'Available')

    equipmet1 = Equipment(1, 'Equipment 1', [gadget1, gadget2])
    equipmet2 = Equipment(2, 'Equipment 2', [gadget3])

    schedule1 = Schedule(1, date(2020, 1, 1), date(2020, 1, 2), 'To Do')
    schedule2 = Schedule(2, date(2020, 2, 3), date(2021, 5, 3), 'In Progress')

    employee1 = Employee(1, 'John', 'Doe', '1234567890',
                         'john.doe@example.com', 'Constructor')
    employee2 = Employee(2, 'Jane', 'Smith', '9876543210',
                         'jane.smith@example.com', 'Constructor')

    paryoll1 = Payroll(1, 'Payroll 1', [employee1, employee2])

    project1 = Project(1, 'Project 1', 'Description 1', [
                       client1, equipmet1, schedule1, paryoll1])

    project1.show_details(0)
