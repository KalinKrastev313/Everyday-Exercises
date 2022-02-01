rounds = int(input())
parking_lot = {}
for i in range(rounds):
    command = input()
    if len(command.split()) == 3:
        _ , username, plate_number = command.split()
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = plate_number
            print(f"{username} registered {parking_lot[username]} succesfully")
    elif len(command.split()) == 2:
        _, username = command.split()
        if not username in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")


for (username, plate_number) in parking_lot.items():
    print(f"{username} => {plate_number}")