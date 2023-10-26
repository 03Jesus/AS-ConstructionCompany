import json
from logic.classes.person import Person


class Employee (Person):
    """
    A class that represents an Employee
    """

    def __init__(self,
                 id: int = 0,
                 name: str = 'name',
                 last_name: str = 'last_name',
                 phone: str = 'phone',
                 mail: str = 'mail',
                 type: str = 'type') -> object:
        """
        Constructor of the class
        :param id: the id of the Employee
        :type id: int
        :param name: the name of the Employee
        :type name: str
        :param last_name: the last name of the Employee
        :type last_name: str
        :param phone: the phone of the Employee
        :type phone: str
        :param mail: the mail of the Employee
        :type mail: str
        :param type: the type of the Employee
        :type type: str
        """
        super().__init__(id, name, last_name, phone, mail)
        self.__type = type

    @property
    def type(self) -> str:
        """
        Getter for the type of the Employee
        :return: the type of the Employee
        :rtype: str
        """
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        """
        Setter for the type of the Employee
        :param type: the new type of the Employee
        :type type: str
        :return: None
        """
        self.__type = type

    def get_name(self) -> str:
        return self.name

    def show_details(self, depth: int) -> None:
        prefix = "  " * depth
        print(f"{prefix}Employee(id={self.id}, name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', mail='{self.mail}', type='{self.type}')")

    def __str__(self) -> str:
        """
        Returns the string representation of an Employee
        :return: the string representation of an Employee
        :rtype: str
        """
        return f"Employee(id={self.id}, name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', mail='{self.mail}', type='{self.type}')"

    def __eq__(self, other: object) -> bool:
        """
        Checks if two Employees are equal
        :param other: the other Employee
        :type other: object
        :return: True if the Employees are equal, False otherwise
        :rtype: bool
        """
        if not isinstance(other, Employee):
            return False
        return self.id == other.id and \
            self.name == other.name and \
            self.last_name == other.last_name and \
            self.phone == other.phone and \
            self.mail == other.mail and \
            self.type == other.type


if __name__ == '__main__':
    em1 = Employee(1, 'name1', 'last_name1', 'phone1', 'mail1', 'type1')
    em2 = Employee(2, 'name2', 'last_name2', 'phone2', 'mail2', 'type2')
    em3 = Employee(3, 'name3', 'last_name3', 'phone3', 'mail3', 'type3')

    assert em1.id == 1

    print(json.dumps(em1.__str__()))

    if em1 == em2:
        print('em1 == em2')
    else:
        print('em1 != em2')
