from enum import Enum

class Department(Enum):
    HR = "Human Resource"
    DEVELOPMENT = "Development"
    DATA_SCIENCE = "Data Science"
    MANAGEMENT = "Management"

class Employee:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

    def __str__(self):
        return f"Employee: ({self.name}, {self.id}, {self.department.value})"

class Manager(Employee):
    def __init__(self, id, name, department):
        super().__init__(id, name, department)
        self.team = list()

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.team.append(employee)
            print(f"{employee.name} assigned to {self.name}")
        else:
            print("No such employee exists.")

    def __len__(self):
        return len(self.team)

    def __str__(self):
        return f"Manager: ({super().__str__()}) | Team size: ({len(self.team)})"

class Developer(Employee):
    def __init__(self, id, name, department, technology):
        super().__init__(id, name, department)
        self.technology = technology

    def update_technology(self, technology):
        self.technology = technology

    def __str__(self):
        return f"Developer: ({super().__str__()}) | Technology: ({self.technology})"
    
class HRManager(Manager):
    def __init__(self, id, name):
        super().__init__(id, name, Department.HR)

class PythonDeveloper(Developer):
    def __init__(self, id, name):
        super().__init__(id, name, Department.DEVELOPMENT, "Python")

class DataScientist(Developer):
    def __init__(self, id, name):
        super().__init__(id, name, Department.DATA_SCIENCE, "Python & SQL")


dev1 = PythonDeveloper(101, "Rohan")
dev2 = DataScientist(102, "Pulkit")
hr_manager = HRManager(200, "Lily")
trainee = DataScientist(202, "Khushal")
hr_manager.add_employee(trainee)
react_dev = Developer(305, "Aayush", Department.DEVELOPMENT, "Javascript")
manager = Manager(300, "David", Department.MANAGEMENT)
manager.add_employee(react_dev)
manager.add_employee(dev1)
manager.add_employee(dev2)


print(dev1)
print(dev2)
print(hr_manager)
print(manager)
print(f"Total Employees under {manager.name}: {len(manager)}")

