import json
from client import Client
from equipment import Equipment
from schedule import Schedule
from payroll import Payroll
from employee import Employee
from gadget import Gadget

class Project (object):
    """
    A class that represents a Project
    """

    def __init__(self,
                 id: int = 0,
                 name: str = 'name',
                 client: Client = Client(),
                 description: str = 'description',
                 equipment: Equipment = Equipment(),
                 schedule: Schedule = Schedule(),
                 payroll: Payroll = Payroll()) -> object:
        """
        Constructor of the class
        :param id: the id of the Project
        :type id: int
        :param name: the name of the Project
        :type name: str
        :param client: the client of the Project
        :type client: Client
        :param description: the description of the Project
        :type description: str
        :param equipment: the equipment of the Project
        :type equipment: Equipment
        :param schedule: the schedule of the Project
        :type schedule: Schedule
        :param payroll: the payroll of the Project
        :type payroll: Payroll
        """
        self.__id = id
        self.__name = name
        self.__client = client
        self.__description = description
        self.__equipment = equipment
        self.__schedule = schedule
        self.__payroll = payroll

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
    def client(self) -> Client:
        """
        Getter for the client of the Project
        :return: the client of the Project
        :rtype: Client
        """
        return self.__client
    
    @client.setter
    def client(self, client: Client) -> None:
        """
        Setter for the client of the Project
        :param client: the new client of the Project
        :type client: Client
        :return: None
        """
        self.__client = client

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
    def equipment(self) -> Equipment:
        """
        Getter for the equipment of the Project
        :return: the equipment of the Project
        :rtype: Equipment
        """
        return self.__equipment
    
    @equipment.setter
    def equipment(self, equipment: Equipment) -> None:
        """
        Setter for the equipment of the Project
        :param equipment: the new equipment of the Project
        :type equipment: Equipment
        :return: None
        """
        self.__equipment = equipment

    @property
    def schedule(self) -> Schedule:
        """
        Getter for the schedule of the Project
        :return: the schedule of the Project
        :rtype: Schedule
        """
        return self.__schedule
    
    @schedule.setter
    def schedule(self, schedule: Schedule) -> None:
        """
        Setter for the schedule of the Project
        :param schedule: the new schedule of the Project
        :type schedule: Schedule
        :return: None
        """
        self.__schedule = schedule

    @property
    def payroll(self) -> Payroll:
        """
        Getter for the payroll of the Project
        :return: the payroll of the Project
        :rtype: Payroll
        """
        return self.__payroll
    
    @payroll.setter
    def payroll(self, payroll: Payroll) -> None:
        """
        Setter for the payroll of the Project
        :param payroll: the new payroll of the Project
        :type payroll: Payroll
        :return: None
        """
        self.__payroll = payroll
        
    def __str__(self) -> str:
        """
        String representation of the Project
        :return: a string containing the Project
        :rtype: str
        """
        return f"Project(id={self.id}, name='{self.name}', client={str(self.client)}, description='{self.description}', equipment={str(self.equipment)}, schedule={str(self.schedule)}, payroll={str(self.payroll)})"
    
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
            self.__client == other.client and \
            self.__description == other.description and \
            self.__equipment == other.equipment and \
            self.__schedule == other.schedule and \
            self.__payroll == other.payroll
    
if __name__ == "__main__":
    client = Client(1,
                "Jesu",
                "last_name",
                "phone",
                "mail")
    
    gadget1 = Gadget(1, 'gadget1', 'type1', 'state1')
    gadget2 = Gadget(2, 'gadget2', 'type2', 'state2')
    gadget3 = Gadget(3, 'gadget3', 'type3', 'state3')

    equipment = Equipment([gadget1, gadget2, gadget3])

    schedule = Schedule(1,
                "start_date",
                "finish_date",
                "state")
    
    em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
    em2 = Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")

    payroll = Payroll([em1, em2])

    project = Project(1,
                "Construction House",
                client,
                "description",
                equipment,
                schedule,
                payroll)
    
    print(project.__str__())    

