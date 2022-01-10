inventory = input().split(", ")
command = ""

while not command == "Craft!":
    next_command = input()
    if not next_command == "Craft!":
        command, item = next_command.split(" - ")
    else:
        command = next_command

    if command == "Collect":
        if not item in inventory:
            inventory.append(item)

    if command == "Drop":
        if item in inventory:
            inventory.remove(item)

    if command == "Combine Items":
        old_item , new_item = item.split(":")
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)

    if command == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

result = ", ".join([str(item) for item in inventory])
print(result)