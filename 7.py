# 7)Extend the above solution again and add another instance method called 'as_dict'. The method should return a dictionary with the data of the student. It should contain 'name', 'score', 'grade', keys and their respective values. 


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.check_grade()

    def check_grade(self):
        if self.score >= 90:
            return 'A+'
        elif 80 <= self.score < 90:
            return 'A'
        elif 70 <= self.score < 80:
            return 'B+'
        elif 60 <= self.score < 70:
            return 'B'
        elif 50 <= self.score < 60:
            return 'C+'
        elif 40 <= self.score < 50:
            return 'C'
        else:
            return 'FAILED'

    def show_details(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Grade:", self.grade)

    def as_dict(self):
        return {
            'name': self.name,
            'score': self.score,
            'grade': self.grade
        }

student1 = Student("Anamika", 36)
student2 = Student("Aamy", 98)

print("Student 1:")
student1.show_details()

print("\nStudent 2:")
student2.show_details()

print("Student 1 as dictionary:", student1.as_dict())
print("Student 2 as dictionary:", student2.as_dict())
