number_of_rooms = int(input())
chairs_left = []

for room in range(number_of_rooms):
    chairs_raw, taken = input().split()
    chairs = len(chairs_raw)
    taken = int(taken)
    chairs_left.append(chairs - taken)
    if chairs - taken < 0:
        print(f"{taken - chairs} more chairs needed in room {room + 1}")

if sum(chairs_left) > 0:
    print(f"Game on, {sum(chairs_left)} free chairs left")