import sys

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

biggest_hourglass = -sys.maxsize

for col in range(4):
    for row in range(4):
        hourglass = sum(arr[row][col:col + 3])
        hourglass += arr[row + 1][col + 1]
        hourglass += sum(arr[row + 2][col:col + 3])
        if hourglass > biggest_hourglass:
            biggest_hourglass = hourglass

print(biggest_hourglass)