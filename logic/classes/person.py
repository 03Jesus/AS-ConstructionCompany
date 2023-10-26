import json
from logic.classes.component import Component


class Person (Component):
    """
    A class that represents a Person
    """

    def __init__(self,
                 id: int = 0,
                 name: str = 'name',
                 last_name: str = 'last_name',
                 phone: str = 'phone',
                 mail: str = 'mail') -> object:
        """
        Constructor of the class
        :param id: the id of the Person
        :type id: int
        :param name: the name of the Person
        :type name: str
        :param last_name: the last name of the Person
        :type last_name: str
        :param phone: the phone of the Person
        :type phone: str
        :param mail: the mail of the Person
        :type mail: str
        """
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__phone = phone
        self.__mail = mail

    @property
    def id(self) -> int:
        """
        Getter for the id of the Person
        :return: the id of the Person
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Person
        :param id: the new id of the Person
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def name(self) -> str:
        """
        Getter for the name of the Person
        :return: the name of the Person
        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for the name of the Person
        :param name: the new name of the Person
        :type name: str
        :return: None
        """
        self.__name = name

    @property
    def last_name(self) -> str:
        """
        Getter for the last name of the Person
        :return: the last name of the Person
        :rtype: str
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """
        Setter for the last name of the Person
        :param last_name: the new last name of the Person
        :type last_name: str
        :return: None
        """
        self.__last_name = last_name

    @property
    def phone(self) -> str:
        """
        Getter for the phone of the Person
        :return: the phone of the Person
        :rtype: str
        """
        return self.__phone

    @phone.setter
    def phone(self, phone: str) -> None:
        """
        Setter for the phone of the Person
        :param phone: the new phone of the Person
        :type phone: str
        :return: None
        """
        self.__phone = phone

    @property
    def mail(self) -> str:
        """
        Getter for the mail of the Person
        :return: the mail of the Person
        :rtype: str
        """
        return self.__mail

    @mail.setter
    def mail(self, mail: str) -> None:
        """
        Setter for the mail of the Person
        :param mail: the new mail of the Person
        :type mail: str
        :return: None
        """
        self.__mail = mail

    def get_name(self) -> str:
        return self.name

    def show_details(self, depth: int) -> None:
        prefix = "  " * depth
        print(f"{prefix}Person(id={self.id}, name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', mail='{self.mail}')")

    def __str__(self) -> str:
        """
        String representation of the Person
        :return: the string representation of the Person
        :rtype: str
        """
        return f"Person(id={self.id}, name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', mail='{self.mail}')"

    def __eq__(self, other: object) -> bool:
        """
        Check if two Persons are equal
        :param other: the other Person
        :type other: object
        :return: True if the Persons are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Person):
            return self.id == other.id and \
                self.name == other.name and \
                self.last_name == other.last_name and \
                self.phone == other.phone and \
                self.mail == other.mail
        return False


if __name__ == '__main__':
    p1 = Person(1, 'name1', 'last_name1', 'phone1', 'mail1')
    p2 = Person(2, 'name2', 'last_name2', 'phone2', 'mail2')
    p3 = Person(1, 'name3', 'last_name3', 'phone3', 'mail3')

    assert p1.id == 1

    print(json.dumps(p1.__str__()))

    if p1 == p2:
        print("p1 == p2")
    else:
        print("p1 != p2")
