text = input()
n = int(input())

result = []
for i in range(0, len(text), len(text)//n):
    word = ""
    for char_index in range(i, i + len(text)//n):
        word += text[char_index]
    result.append(word)

print(result)