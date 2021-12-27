first_number = int(input())
second_number = int(input())

def division_of_factorials (num1, num2):
    num1_factorial = 1
    num2_factorial = 1
    for number in range(2, num1 +1):
        num1_factorial = num1_factorial * number
    for factor in range(2, num2 +1):
        num2_factorial = num2_factorial * factor
    result = float(num1_factorial/num2_factorial)
    print(f"{result:.2f}")

division_of_factorials(first_number, second_number)