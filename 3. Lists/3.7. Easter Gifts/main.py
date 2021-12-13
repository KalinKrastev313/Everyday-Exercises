list_of_gifts = input().split()
next_command = []
n = 1
while n == 1:
    next_command = input().split()
    if next_command == "No Money":
        break
    if next_command[0] == "OutOfStock":
        for item in range(0, len(list_of_gifts)):
            if list_of_gifts[item] == next_command[1]:
                list_of_gifts[item] = None
    elif next_command[0] == "Required":
        if int(next_command[2]) <= len(list_of_gifts) - 1:
            list_of_gifts[int(next_command[2])] = next_command[1]
    elif next_command[0] == "JustInCase":
        list_of_gifts[len(list_of_gifts) - 1] = next_command[1]
    next_command = []
print(list_of_gifts)