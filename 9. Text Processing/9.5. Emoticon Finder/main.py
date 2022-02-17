text = input().split()
characters = []
for word in text:
    if ":" in word:
        for char in word:
            characters.append(char)
        print(f":{word[characters.index(':')+1]}")
    characters = []