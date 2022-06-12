text = input()
result = ""

for char in text:
    if char == "y":
        result += "a"
    elif char == "z":
        result += "b"
    else:
        result += chr(ord(char) + 2)

print(result)