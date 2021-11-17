quantity = int(input())
days = int(input())
total_cost = 0
total_spirit = 0
ornament_set_bought = 0
tree_skirts_bought = 0
tree_garlands_bought = 0

for day in range (1, days + 1, 1):

    if day % 2 == 0:
        total_cost += quantity * 2
        total_spirit += 5
        ornament_set_bought = 1

    if day % 3 == 0:
        total_cost += quantity * (5+3)
        total_spirit += 13
        tree_skirts_bought = 1
        tree_garlands_bought = 1

    if day % 5 == 0 :
        total_cost += quantity * 15
        total_spirit += 17
        if tree_skirts_bought == 1 and tree_garlands_bought == 1:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += 1 * (5 + 3 + 15)
        # Gorniqt red ne e siguren
        # quantity += 2

    if day % 11 == 0:
        quantity += 2

    ornament_set_bought = 0
    tree_skirts_bought = 0
    tree_garlands_bought = 0

if days % 10 == 0:
    total_spirit -= 30


print("Total cost: " + str(total_cost))
print("Total spirit: " + str(total_spirit))