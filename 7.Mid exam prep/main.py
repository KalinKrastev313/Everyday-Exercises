def target_decreace(target_index, points):
    if targets[target_index] - 5 >= 0:
        points += 5
        targets[target_index] -= 5
    else:
        points += targets[target_index]
        target_index[target_index] = 0
    return points

def shoot_left(start_i, length, points):
    points = target_decreace(start_i - length, points)
    return points

def shoot_right(start_i, length, points):
    if start_i + length <= len(targets):
        points = target_decreace(start_i + length, points)
    else:
        points = target_decreace(start_i + length - len(targets), points)
    return points


targets = [int(i) for i in input().split("|")]
command = input()
points = 0

while not command == "Game over":
    if command == "Reverse":
        targets.reverse()
    else:
        order, start_index, length = command.split("@")
        start_index = int(start_index)
        length = int(length)
        while length > len(targets):
            length -= len(targets)
        if start_index in range(len(targets)):
            if order == "Shoot Left":
                points = shoot_left(start_index, length, points)
            if order == "Shoot Right":
                points = shoot_right(start_index, length, points)

    command = input()


print(f"{' - '.join([str(i) for i in targets])}\n"
      f"Iskren finished the tournament with {points} points!")
