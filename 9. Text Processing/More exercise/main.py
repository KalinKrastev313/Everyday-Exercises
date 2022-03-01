lines = int(input())

for num in range(lines):
    text = input()
    name = text[text.index("@") + 1:text.index("|")]
    age = text[text.index("#") + 1:text.index("*")]
    print(f"{name} is {age} years old.")