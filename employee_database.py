class EmployeeDatabase:
    
    def __init__(self):
        self.employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def displayEmployees(self):
        for employee in self.employees:
            employee.display()
            print()
