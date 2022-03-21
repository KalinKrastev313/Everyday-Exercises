class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"

    def get_name(self):
        return self.name


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if not pokemon in self.pokemon:
            self.pokemon.append(pokemon)
            result = "Caught " + pokemon.pokemon_details()
            return f"{result}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for creature in self.pokemon:
            if creature.get_name() == pokemon_name:
                self.pokemon.remove(creature)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for creature in self.pokemon:
            result += "- " + creature.pokemon_details() + f"\n"
        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())