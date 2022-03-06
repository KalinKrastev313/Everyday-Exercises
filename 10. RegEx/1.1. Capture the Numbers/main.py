import re

text = input()
x = "\d+"
pattern = re.findall(x, text)
print(" ".join(pattern))