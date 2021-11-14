print("This program returns the higher number which is lower \n than a given bound and divisible by a given divisor \n")
print("Enter the upper bound \n")
Bound = int(input())
print("Enter the divisor \n")
Divisor = int(input())
result = ""

for number in range (Bound, 0, -1):

    for division_result in range (1, Bound, 1):
        if number/division_result == Divisor :
            result =+ number
            break
    if result != "":
        break

print(result)