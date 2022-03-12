import re

data = input()
pattern = r"(^|(?<=\s))w{3}\.[\w+|-]+(\.[a-z]+)+($|(?=\s))"

while data:
    for addres in re.finditer(pattern, data):
        print(addres.group())
    data = input()