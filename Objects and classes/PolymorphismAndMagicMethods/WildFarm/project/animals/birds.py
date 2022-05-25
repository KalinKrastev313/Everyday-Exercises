from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    def __init__(self, name, weight, wing_size, food_eaten = 0):
        super().__init__(name, weight, food_eaten, wing_size)
        self.wing_size = wing_size

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}"



class Hen(Bird):
    def __init__(self, name, weight, wing_size, food_eaten = 0):
        super().__init__(name, weight, food_eaten, wing_size)
        self.wing_size = wing_size

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity
