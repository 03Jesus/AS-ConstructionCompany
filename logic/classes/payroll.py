from typing import List

from logic.classes.component import Component
from logic.classes.employee import Employee
from logic.classes.list_component import ListComponent


class Payroll (ListComponent):
    """
    A class that represents a Payroll (a list of employees)
    """

    def __init__(self,
                 id: int = 0,
                 name: str = "name",
                 employees: List[Employee] = None) -> ListComponent:
        """
        Constructor for the Payroll class
        :param id: the id of the Payroll
        :type id: int
        :param employees: the list of employees of the Payroll
        :type employees: List[Employee]
        """
        self.__id = id
        self.__name = name
        if employees is None:
            self.__employees = []
        else:
            self.__employees = employees

    @property
    def id(self) -> int:
        """
        Getter for the id of the Payroll
        :return: the id of the Payroll
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Payroll
        :param id: the new id of the Payroll
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def name(self) -> str:
        """
        Getter for the name of the Payroll
        :return: the name of the Payroll
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for the name of the Payroll
        :param name: the new name of the Payroll
        :type name: str
        :return: None
        """
        self.__name = name

    @property
    def employees(self) -> List[Employee]:
        """
        Getter for the employees of the Payroll
        :return: the employees of the Payroll
        :rtype: List[Employee]
        """
        return self.__employees

    @employees.setter
    def employees(self, employees: List[Employee]) -> None:
        """
        Setter for the employees of the Payroll
        :param employees: the new employees of the Payroll
        :type employees: List[Employee]
        :return: None
        """
        self.__employees = employees

    def add_child(self, child: Employee) -> None:
        """
        Adds a child to the Payroll
        :param child: the child to add
        :type child: Employee
        :return: None
        """
        self.employees.append(child)

    def remove_child(self, child: Employee) -> None:
        """
        Removes a child from the Payroll
        :param child: the child to remove
        :type child: Employee
        :return: None
        """
        self.employees.remove(child)

    def get_name(self) -> str:
        return self.name

    def show_details(self, depth: int) -> None:
        prefix = "  " * depth
        print(f"{prefix}Payroll(id={self.id}, name='{self.name}')")
        for employee in self.employees:
            employee.show_details(depth + 1)

    def __str__(self) -> str:
        """
        Returns the string representation of a Payroll
        :return: the string representation of a Payroll
        :rtype: str
        """
        return f"Payroll(id={self.id}, name='{self.name}')"

    def __eq__(self, other: object) -> bool:
        """
        Checks if two Payrolls are equal
        :param other: the other Payroll
        :type other: object
        :return: True if the Payrolls are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Payroll):
            return self.id == other.id
        return False


if __name__ == "__main__":
    payroll = Payroll(1, 'name')
    payroll2 = Payroll(2, 'Payroll2')
    payroll.show_details(0)
    print(payroll == payroll2)
