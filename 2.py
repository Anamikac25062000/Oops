# 2)Write a program that prints the class name using its object. 


class Employee:
    def __init__(self, name, position, company):
        self.name = name
        self.position = position
        self.company = company

an_employee = Employee("Anamika C", "Software Engineer", "Beinex")

print("Class name:", an_employee.__class__.__name__)
