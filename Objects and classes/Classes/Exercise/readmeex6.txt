Solution of the following exercise: 

Pokemon Battle
You are tasked to create two classes: a Pokemon class and a Trainer class. The Pokemon class should receive a name (string) and health (int) upon initialization. It should also have a method called pokemon_details that returns the information of the pokemon:  "{pokemon_name} with health {pokemon_health}"
The Trainer class should receive a name (string). The Trainer should also have an attribute pokemon (list, empty by default). The Trainer has three methods:
add_pokemon(pokemon: Pokemon)
Add the pokemon to the collection. After adding the pokemon, it should return "Caught {pokemon_name} with health {pokemon_health}". Note: use the pokemon's details method.
If the pokemon is already in the collection, it should return "This pokemon is already caught"
release_pokemon(pokemon_name: String) 
Check if you have a pokemon with the name and remove it from the collection. It should return "You have released {pokemon_name}"
If there isn't a pokemon with that name in the collection, return "Pokemon is not caught"
trainer_data()
The method returns the information of the trainer with his pokemon in this format:
"Pokemon Trainer {trainer_name}
 Pokemon count {the amount of pokemon caught}
 - {pokemon_details}
 ...
 - {pokemon_details}
"

Examples
Test Code	
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

Output
Pikachu with health 90
Caught Pikachu with health 90
Caught Charizard with health 110
This pokemon is already caught
You have released Pikachu
Pokemon is not caught
Pokemon Trainer Ash
Pokemon count 1
- Charizard with health 110

