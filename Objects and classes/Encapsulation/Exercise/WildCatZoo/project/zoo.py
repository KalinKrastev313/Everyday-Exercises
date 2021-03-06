class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
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
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except KeyError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_sum = sum([w.salary for w in self.workers])
        if self.__budget >= salaries_sum:
            self.__budget -= salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_needs_cost = sum([a.get_needs() for a in self.animals])
        if self.__budget >= animals_needs_cost:
            self.__budget -= animals_needs_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions\n"
        result += "{}".format('\n'.join([repr(l) for l in lions])) + "\n"
        result += f"----- {len(tigers)} Tigers\n"
        result += "{}".format('\n'.join([repr(l) for l in tigers])) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs\n"
        result += "{}".format('\n'.join([repr(l) for l in cheetahs])) + "\n"
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        result += "{}".format(("\n").join([repr(w) for w in keepers])) + '\n'
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "{}".format(("\n").join([repr(w) for w in caretakers])) + '\n'
        result += f"----- {len(vets)} Vets:\n"
        result += "{}".format(("\n").join([repr(w) for w in vets])) + '\n'

        return result