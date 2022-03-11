import re

command = input()
text = ""
cost = 0

while not command == "Purchase":
    text += command
    command = input()


pattern = ">>(?P<furniture>\w+)<<(?P<price>[\d|\.]+)!(?P<quantity>\d+)"
info = re.findall(pattern, text)

print("Bought furniture:")

for item in info:
    cost += float(item[1])*int(item[2])
    print(item[0])

print(f"Total money spent: {cost}")