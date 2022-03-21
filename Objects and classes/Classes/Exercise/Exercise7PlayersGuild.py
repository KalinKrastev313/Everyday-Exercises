class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def change_guild(self, new_guild):
        self.guild = new_guild

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        else:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for skill in self.skills:
            result += f"==={skill} - {self.skills[skill]}"
        return result


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            player.change_guild(self.name)
            self.list_of_players.append(player)
            return f"Welcome {player.name} to the guild {self.name}"
        elif player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild"

    def kick_player(self, player):
        for player in self.list_of_players:
            if player.name == player:
                self.list_of_players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player.name} has been removed from the guild"
        return f"Player {player.name} is not in the guild"

    def guild_info(self):
        result = f"Guild: {self.name}"
        for char in self.list_of_players:
            result += char.player_info()
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
