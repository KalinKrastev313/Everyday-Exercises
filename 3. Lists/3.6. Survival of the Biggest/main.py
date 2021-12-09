numbers_collection = input().split()
for index in range(len(numbers_collection)):
    numbers_collection[index] = int(numbers_collection[index])
n = int(input())
for number in range(n):
    numbers_collection.remove(min(numbers_collection))

print(numbers_collection)