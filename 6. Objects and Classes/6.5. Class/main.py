class Class:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        self.students.append(name)
        self.grades.append(float(grade))

    def get_average_grade(self):
        return round(sum((self.grades))/len(self.grades), 2)

    def __repr__(self):
        students_joined = ", ".join(self.students)
        return f"The students in {self.name}: {students_joined}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)