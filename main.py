from developer import Developer
from manager import Manager
from tester import Tester
from employee_database import EmployeeDatabase

# create developer data
d1 = Developer("Elvin", 20000, "Associate Software Engineer")

# print d1 info
print("d1 info before update")
d1.display()

# update d1 info
d1.updateRole("Software Engineer")
d1.updateSalary(35000)
d1.updateName("Elvin Rajkumar")
d1.updateDepartment("R&D")

# print d1 info post update
print("d1 info post update")
d1.display()

# create manager data
m1 = Manager("David", 25000, "Technical Lead")

# print d1 info
print("m1 info before update")
m1.display()

# update m1 info
m1.updateRole("Senior Technical Lead")
m1.updateSalary(45000)
m1.updateName("David Gayler")
m1.updateDepartment("R&D")

# print m1 info post update
print("m1 info post update")
m1.display()

# create tester data
t1 = Tester("Rohit", 12000)

# print t1 info
print("t1 info before update")
t1.display()

# update t1 info
t1.updateRole("Associate Software Tester")
t1.updateSalary(25000)
t1.updateName("Rohit Kumar")
t1.updateDepartment("Web App team")

# print t1 info post update
print("t1 info post update")
t1.display()

# create employee database
empDB = EmployeeDatabase()

# add d1, m1 and t1 to employee database
print("Add d1, m1 and t1 to empDB")
empDB.addEmployee(d1)
empDB.addEmployee(m1)
empDB.addEmployee(t1)

# print employee list
print("empDB post adding d1, m1 and t1")
empDB.displayEmployees()