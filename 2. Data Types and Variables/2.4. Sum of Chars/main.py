print("Enter n")
n = int(input())
all_letters = []
for number in range (0, n, 1):
    all_letters.append(input())

turned_to_numbers = []
for char in all_letters:
    turned_to_numbers.append(ord(char))

print(sum(turned_to_numbers))