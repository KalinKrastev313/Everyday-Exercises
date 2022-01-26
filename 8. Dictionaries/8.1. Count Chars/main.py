characters = {}

text = input()
for char in range(len(text)):
    if text[char] in characters:
        characters[text[char]] += 1
    else:
        if not text[char] == " ":
            characters[text[char]] = 1

for (key, value) in characters.items():
    print(f"{key} -> {value}")