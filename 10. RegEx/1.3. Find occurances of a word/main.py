import re

text = input()
word = input()
pattern = ""

for char in word:
    pattern += "["
    if char.islower():
        pattern += char
        pattern += "|"
        pattern += chr(ord(char) - 32)
        pattern += "]"
    else:
        pattern += char
        pattern += "|"
        pattern += chr(ord(char) + 32)
        pattern += "]"

pattern += "[ |!|?|.]"

print(len(re.findall(pattern,text)))