lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
cost = 0

for n_fight in range (1, lost_fights_count, 1):

    if n_fight % 2 == 0:
        cost += helmet_price

    if n_fight % 3 == 0:
        cost += sword_price

    if n_fight % 6 == 0:
        cost += shield_price

    if n_fight % 12 == 0:
        cost += armor_price

print(cost)