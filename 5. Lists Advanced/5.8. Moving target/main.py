targets_str = input().split()
targets = [int(item) for item in targets_str]
command = ""

while not command == "End":
    full_command = input().split()
    command = full_command[0]
    if len(full_command) == 3:
        full_command[1] = int(full_command[1])
        full_command[2] = int(full_command[2])

    if command == "Shoot" and full_command[1] <= len(targets) -1:
        targets[full_command[1]] -= full_command[2]
        if targets[full_command[1]] <= 0:
            targets.pop(full_command[1])

    if command == "Add":
        if full_command[1] <= len(targets) -1:
            targets.insert(full_command[1], full_command[2])
        else:
            print("Invalid placement")

    if command == "Strike":
        if 0 <= full_command[1] - full_command[2] and full_command[1] + full_command[2] <= len(targets) -1:
            del targets[full_command[1] - full_command[2]:full_command[1] + full_command[2] + 1]
        else: print("Strike missed!")

result = "|".join([str(item) for item in targets])
print(result)