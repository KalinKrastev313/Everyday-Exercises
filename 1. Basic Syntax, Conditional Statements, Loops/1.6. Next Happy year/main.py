year = input()
result = int(year) + 1

while len(year) > len(set(str(result))):
    result += 1

print(result)