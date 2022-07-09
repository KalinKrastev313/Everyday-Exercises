n = 125
binary = ""
while n > 0:
    binary += str(n%2)
    n = n//2

consecutive = 0
new_consecutive = 0
for char in binary:
    if char == "1":
        new_consecutive += 1
    else:
        new_consecutive = 0

    if new_consecutive > consecutive:
        consecutive = new_consecutive

print(consecutive)