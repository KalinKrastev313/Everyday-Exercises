def sum_of_digits(num):
    even_digits = []
    odd_digits = []
    for index in range (0, len(num)):
        if int(num[index]) % 2 == 0:
            even_digits.append(int(num[index]))
        else:
            odd_digits.append(int(num[index]))
    return sum(odd_digits), sum(even_digits)

number = input()
odd_digits_sum, even_digits_sum = sum_of_digits(number)
print(f"Odd sum = {odd_digits_sum}, Even sum = {even_digits_sum}")