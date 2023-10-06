import json
from datetime import date
class Schedule (object):
    """
    A class that represents a Schedule
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
        :param start_date: the start date of the Schedule
        :type start_date: date
        :param finish_date: the finish date of the Schedule
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
        Getter for the start date of the Schedule
        :return: the start date of the Schedule
        :rtype: date
        """
        return self.__start_date
    
    @start_date.setter
    def start_date(self, start_date: date) -> None:
        """
        Setter for the start date of the Schedule
        :param start_date: the new start date of the Schedule
        :type start_date: date
        :return: None
        """
        self.__start_date = start_date

    @property
    def finish_date(self) -> date:
        """
        Getter for the finish date of the Schedule
        :return: the finish date of the Schedule
        :rtype: date
        """
        return self.__finish_date
    
    @finish_date.setter
    def finish_date(self, finish_date: date) -> None:
        """
        Setter for the finish date of the Schedule
        :param finish_date: the new finish date of the Schedule
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

    def __str__(self) -> str:
        """
        Returns the string representation of a Schedule
        :return: the string representation of a Schedule
        :rtype: str
        """
        return f"Schedule(id={self.id}, start_date='{self.start_date}', finish_date='{self.finish_date}', state='{self.state}')"
    
    def __eq__(self, other: object) -> bool:
        """
        Method that compares two Schedules
        :param other: the other Schedule
        :type other: object
        :return: True if the Schedules are equal, False otherwise
        :rtype: bool
        """
        if not isinstance(other, Schedule):
            return False
        return self.__id == other.id and \
               self.__start_date == other.start_date and \
               self.__finish_date == other.finish_date and \
               self.__state == other.state
    
if __name__ == "__main__":
    schedule = Schedule(1, date.today(), date.today(), 'state')
    print(schedule)
    print(schedule.id)
    print(schedule.start_date)
    print(schedule.finish_date)
    print(schedule.state)
    print(schedule == Schedule(1, date.today(), date.today(), 'state'))
    print(schedule == Schedule(2, date.today(), date.today(), 'state'))
    print(schedule == Schedule(1, date.today(), date.today(), 'state2'))