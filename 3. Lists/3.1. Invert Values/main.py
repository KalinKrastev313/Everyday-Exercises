numbers_collection = input()
first_collection = numbers_collection.split()
for index in range(len(first_collection)):
    first_collection[index] = (int(first_collection[index]))*(-1)

print(first_collection)