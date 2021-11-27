n = int(input())
capacity = 255
filled = 0

for number in range (0, n, 1):
    pour = int(input())
    if filled + pour < capacity:
        filled += pour
    else:
        print("Insufficient capacity")

print(filled)