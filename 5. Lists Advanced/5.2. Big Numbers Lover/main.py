numbers = input().split()

result = [str(item) for item in numbers]
result = list(sorted(result, key= lambda x: x[0], reverse=True))
print(result)
