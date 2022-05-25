from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    def __init__(self, name, weight, living_region, food_eaten = 0):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ == "Vegetable" or "Fruit":
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}"

class Dog(Mammal):
    def __init__(self, name, weight, living_region, food_eaten = 0):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}"


class Cat(Mammal):
    def __init__(self, name, weight, living_region, food_eaten = 0):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ == "Meat" or "Vegetable":
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region, food_eaten = 0):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}"