import json
from person import Person


class Administrator (Person):
    """
    A class that represents an Administrator
    """

    def __init__(self,
                 id: int = 0,
                 name: str = 'name',
                 last_name: str = 'last_name',
                 phone: str = 'phone',
                 mail: str = 'mail',) -> object:
        """
        Constructor of the class
        :param id: the id of the Administrator
        :type id: int
        :param name: the name of the Administrator
        :type name: str
        :param last_name: the last name of the Administrator
        :type last_name: str
        :param phone: the phone of the Administrator
        :type phone: str
        :param mail: the mail of the Administrator
        :type mail: str
        :param password: the password of the Administrator
        :type password: str
        """
        super().__init__(id, name, last_name, phone, mail)

    def __str__(self) -> str:
        """
        Method that returns the string representation of the Administrator
        :return: the string representation of the Administrator
        :rtype: str
        """
        return f"Administrator: {self.id}, {self.name}, {self.last_name}, {self.phone}, {self.mail}"

    def __eq__(self, other: object) -> bool:
        """
        Method that checks if two Administrators are equal
        :param other: the other Administrator
        :type other: object
        :return: True if the Administrators are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Administrator):
            return self.id == other.id and \
                self.name == other.name and \
                self.last_name == other.last_name and \
                self.phone == other.phone and \
                self.mail == other.mail
        return False


if __name__ == '__main__':
    administrator = Administrator(1, 'name', 'last_name', 'phone', 'mail')
    administrator2 = Administrator(1, 'name', 'last_name', 'phone', 'mail')
    print(json.dumps(administrator.__str__()))

    if administrator == administrator2:
        print('administrator1 == administrator2')
    else:
        print('administrator1 != administrator2')