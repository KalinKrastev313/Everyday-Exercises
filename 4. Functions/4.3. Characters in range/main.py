first_character = input()
second_character = input()

def print_in_between (a, b):
    result = []
    for number in range (ord(a) + 1, ord(b)):
        result.append(chr(number))
    return result

print(print_in_between(first_character, second_character))