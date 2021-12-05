factor = int(input())
count = int(input())
result = []

while len(result) < count:
    result.append((len(result)+1)*factor)

print(result)