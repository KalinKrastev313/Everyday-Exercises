side = int(input())

print("* "*side)
for number in range(0, side -2):
    print("*" + "  "*(side-2) + " *")
print("* "*side)