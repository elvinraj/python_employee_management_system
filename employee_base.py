from abc import ABC, abstractmethod;

class Employee(ABC):
    
    def __init__(self, employeeId, name, salary):
        self.employeeId = employeeId
        self.name = name
        self.salary = salary
        self.role = ""
        super().__init__()

    @abstractmethod
    def updateRole(self, role):
        self.role = role

    @abstractmethod
    def updateSalary(self):
        pass
    
    @abstractmethod
    def updateName(self):
        pass

    @abstractmethod
    def display(self):
        print("Id :", self.employeeId)
        print("Name :", self.name)
        print("Salary :", self.salary)
        print("Role :", self.role)


