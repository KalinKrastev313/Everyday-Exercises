houses_stats = [int(item) for item in input().split("@")]
print(houses_stats)

command = input()
#This is position according to index, not according to the output. For output add 1
position = 0
failed_houses = 0

while not command == "Love!":
    length = int(command[len(command)-1])
    position += length
    if position in range(len(houses_stats)):
        houses_stats[position] -= 2
    else:
        position = 0
        houses_stats[position] -= 2
    if houses_stats[position] == 0:
        print(f"Place {position} has Valentine's day.")
    elif houses_stats[position] < 0:
        print(f"Place {position} already had Valentine's day.")

    command = input()

for item in range(len(houses_stats)):
    if houses_stats[item] > 0:
        failed_houses += 1

print(f"Cupid's last position was {position}.")
print(f"Cupid has failed {failed_houses} places.")
print(houses_stats)