# 1)Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object. 


class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Students("Anamika C", 23, "A+")
student2 = Students("Aamy", 24, "A")

print("Name:", student1.name)
print("Age:", student1.age)
print("Grade:", student1.grade)

print("Name:", student2.name)
print("Age:", student2.age)
print("Grade:", student2.grade)