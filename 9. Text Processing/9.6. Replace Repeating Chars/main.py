text = input()
result = text[0]
for char in range(1, len(text)):
    if not text[char] == text[char - 1]:
        result += text[char]

print(result)