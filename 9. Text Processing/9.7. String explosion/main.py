text = input()
result = ""
explosion_size = 0
for char in range(len(text)):
    if text[char] == ">":
        result += ">"
        next_explosion = ""
        for index in range(char + 1, len(text)):
            if text[index].isdigit():
                next_explosion += text[index]
            else:
                explosion_size += int(next_explosion)
                break
    elif explosion_size > 0:
        explosion_size -= 1
    else:
        result += text[char]

print(result)

