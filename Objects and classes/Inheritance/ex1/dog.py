from ex1.animal import Animal


class Dog(Animal):
    def bark(self):
        return "barking"

dog = Dog()
print(dog.eat())