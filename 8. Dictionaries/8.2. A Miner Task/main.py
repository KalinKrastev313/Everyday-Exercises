command = input()
res = {}
while not command == "stop":
    if command in res:
        res[command] += int(input())
    else:
        res[command] = int(input())

    command = input()

for (key, value) in res.items():
    print(f"{key} -> {value}")