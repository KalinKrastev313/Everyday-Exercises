lower_bound = ord(input())
upper_bound = ord(input())
text = input()
sum_of_characters = 0

for char in text:
    if ord(char) in range(lower_bound + 1, upper_bound):
        sum_of_characters += ord(char)

print(sum_of_characters)