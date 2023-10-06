from employee import Employee

class Payroll (object):
    """
    A class that represents a Payroll (list of employees)
    """

    def __init__(self, employees=None) -> object:
        """
        Constructor of the class
        :param employees: the list of employees
        :type employees: list
        """
        if employees is None:
            self.__employees = []
        else:
            self.__employees = employees

    @property
    def employees(self) -> list:
        """
        Getter for the list of employees
        :return: the list of employees
        :rtype: list
        """
        return self.__employees
    
    @employees.setter
    def employees(self, employees: list) -> None:
        """
        Setter for the list of employees
        :param employees: the new list of employees
        :type employees: list
        :return: None
        """
        self.__employees = employees

    def add_employee(self, employee: Employee) -> None:
        """
        Adds an employee to the list of employees
        :param employee: the employee to add
        :type employee: Employee
        :return: None
        """
        self.employees.append(employee)

    def remove_employee(self, employee: Employee) -> None:
        """
        Removes an employee from the list of employees
        :param employee: the employee to remove
        :type employee: Employee
        :return: None
        """
        self.employees.remove(employee)

    def __str__(self) -> str:
        """
        Returns the string representation of a Payroll
        :return: the string representation of a Payroll
        :rtype: str
        """
        employees_str = ""
        for employee in self.employees:
            employees_str += str(employee) + "\n"
        return f"Payroll(employees=[\n{employees_str}])"
    
    
    def __eq__(self, other: object) -> bool:
        """
        Checks if two Payrolls are equal
        :param other: the other Payroll
        :type other: object
        :return: True if the Payrolls are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Payroll):
            return self.employees == other.employees
        return False
    
if __name__ == "__main__":
    em1 = Employee(1, "Juan", "Perez", "12345678", "juan@perez.com", "constructor")
    em2 = Employee(2, "Pedro", "Gomez", "87654321", "pedro@gomez.com", "constructor")
    
    payroll = Payroll([em1, em2])

    print(payroll)

    payroll.add_employee(Employee(3, "Maria", "Lopez", "12345678", "maria@lopez.com", "constructor"))

    print(payroll)

    payroll.remove_employee(em1)

    print(payroll)

    if payroll == Payroll([em2, Employee(3, "Maria", "Lopez", "12345678", "maria@lopez.com", "constructor")]):
        print("payroll == payroll2")
    else:
        print("payroll != payroll2")