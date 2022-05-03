from ex2.employee import Employee
from ex2.person import Person


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return "teaching..."


teacher = Teacher

print(teacher.teach())
print(teacher.sleep())
print(teacher.get_fired())
