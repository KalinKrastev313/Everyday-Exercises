energy = 100
coins = 100
events = input().split("|")
broke = False

for item in events:
    event_ingredient, number = item.split("-")
    number = int(number)
    if event_ingredient == "rest":
        if energy + number <= 100:
            energy += number
            print(f"You gained {number} energy")
        else:
            print(f"You gained {100 - energy} energy")
            energy = 100
    elif event_ingredient == "order":
        if energy >= 30:
            coins += number
            print(f"You earned {number} coins")
            energy -= 30
        else:
            energy += 50
            print("You had to rest")
    else:
        coins -= number
        if coins > 0:
            print(f"You bought {event_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient}")
            broke = True
            break
if broke is False:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")

collection = [1, 2, 3, 6, 7, 8]
d = collection
collection.append(9)
print(d)