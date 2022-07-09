class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        result = sum(self.scores) / len(self.scores)
        if 90 <= result <= 100:
            return "O"
        elif 80 <= result < 90:
            return "E"
        elif 70 <= result < 80:
            return "A"
        elif 55 <= result < 70:
            return "P"
        elif 40 <= result < 55:
            return "D"
        elif result < 40:
            return "T"