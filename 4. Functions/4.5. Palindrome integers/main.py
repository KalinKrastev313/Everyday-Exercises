first_collection = input().split(", ")

def palindrome_checker(collection_of_numbers):
    flipped_numbers = []
    new_item = ""
    result = []
    for item in collection_of_numbers:
        for index in range (len(item) -1, -1, -1):
            new_item += item[index]
        flipped_numbers.append(new_item)
        new_item = ""
    for index in range (0, len(flipped_numbers)):
        if flipped_numbers[index] == collection_of_numbers[index]:
            result.append(True)
        else:
            result.append(False)
    return result

print(palindrome_checker(first_collection))