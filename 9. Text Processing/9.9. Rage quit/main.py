rant = input()

rant_parts = []
previous_index = 0

# Needs correction for if the number is two or more digits.
for char in rant:
    if char.isdigit():
        rant_parts.append(rant[previous_index:rant.index(char)])
        rant_parts.append(rant[rant.index(char)])
        previous_index = rant.index(char) + 1

for text in range(0, len(rant_parts), 2):
    rant_parts[text] = rant_parts[text].upper()

for num in range(1, len(rant_parts), 2):
    print(int(rant_parts[num])*(rant_parts[num -1]), end="")