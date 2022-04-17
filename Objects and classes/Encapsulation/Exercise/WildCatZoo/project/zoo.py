class Zoo:
    def __init__(self, animal_capacity, workers_capacity, budget, name, animals, workers):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return "Not enough budget"
        elif len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        else:
            self.animals.append(animal)
            self.__budget -= price
            return f"{self.name} the {animal.__class__.__name__} added to the zoo"


