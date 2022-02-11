def lenhgt_checker(name):
    if len(name) in range (3, 17):
        return True

def char_checker(name):
    if name.isalnum():
        return True
    for char in name:
        if not (char.isdigit() or char.isalpha() or char == "-" or char == "_"):
            return False
    return True

list_of_words = input().split(", ")

for word in list_of_words:
    if lenhgt_checker(word) and char_checker(word):
        print(word)