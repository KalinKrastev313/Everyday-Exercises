from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight, food_eaten = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten


class Bird(Animal):
    def __init__(self, name, weight, food_eaten, wing_size):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

class Mammal(Animal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass