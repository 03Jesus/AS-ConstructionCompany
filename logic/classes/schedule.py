from logic.classes.component import Component
from datetime import date


class Schedule (Component):
    """
    A class that represents an Schedule
    """

    def __init__(self,
                 id: int = 0,
                 start_date: date = date.today(),
                 finish_date: date = date.today(),
                 state: str = 'state') -> object:
        """
        Constructor of the class
        :param id: the id of the Schedule
        :type id: int
        :param start_date: the start_date of the Schedule
        :type start_date: date
        :param finish_date: the finish_date of the Schedule
        :type finish_date: date
        :param state: the state of the Schedule
        :type state: str
        """
        self.__id = id
        self.__start_date = start_date
        self.__finish_date = finish_date
        self.__state = state

    @property
    def id(self) -> int:
        """
        Getter for the id of the Schedule
        :return: the id of the Schedule
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Schedule
        :param id: the new id of the Schedule
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def start_date(self) -> date:
        """
        Getter for the start_date of the Schedule
        :return: the start_date of the Schedule
        :rtype: date
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date: date) -> None:
        """
        Setter for the start_date of the Schedule
        :param start_date: the new start_date of the Schedule
        :type start_date: date
        :return: None
        """
        self.__start_date = start_date

    @property
    def finish_date(self) -> date:
        """
        Getter for the finish_date of the Schedule
        :return: the finish_date of the Schedule
        :rtype: date
        """
        return self.__finish_date

    @finish_date.setter
    def finish_date(self, finish_date: date) -> None:
        """
        Setter for the finish_date of the Schedule
        :param finish_date: the new finish_date of the Schedule
        :type finish_date: date
        :return: None
        """
        self.__finish_date = finish_date

    @property
    def state(self) -> str:
        """
        Getter for the state of the Schedule
        :return: the state of the Schedule
        :rtype: str
        """
        return self.__state

    @state.setter
    def state(self, state: str) -> None:
        """
        Setter for the state of the Schedule
        :param state: the new state of the Schedule
        :type state: str
        :return: None
        """
        self.__state = state

    def get_name(self) -> str:
        return str(self.id)

    def show_details(self, depth: int) -> None:
        prefix = "  " * depth
        print(f"{prefix}Schedule(id={self.id}, start_date='{self.start_date}', finish_date='{self.finish_date}' state='{self.state}')")

    def __str__(self) -> str:
        return f"Schedule(id={self.id}, start_date='{self.start_date}', finish_date='{self.finish_date}', state='{self.state}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Schedule):
            return False
        return self.id == other.id and self.start_date == other.start_date and self.finish_date == other.finish_date and self.state == other.state


if __name__ == "__main__":
    s1 = Schedule(1, date(2020, 1, 1), date(2020, 1, 2), 'state1')
    s2 = Schedule(1, date(2020, 1, 1), date(2020, 1, 2), 'state1')
    s3 = Schedule(2, date(2020, 1, 1), date(2020, 1, 2), 'state1')
    s4 = Schedule(1, date(2020, 1, 3), date(2020, 1, 2), 'state1')
    s5 = Schedule(1, date(2020, 1, 1), date(2020, 1, 3), 'state1')
    s6 = Schedule(1, date(2020, 1, 1), date(2020, 1, 2), 'state2')
    s1.show_details(0)
    s3.get_name()
    print(s3)
    print(s4)
    print(s5)
    print(s6)
    print(s1 == s2)
    print(s1 == s3)
    print(s1 == s4)
    print(s1 == s5)
    print(s1 == s6)
    print(s1 == 1)
    print(s1 == 'abc')
    print(s1 == None)
