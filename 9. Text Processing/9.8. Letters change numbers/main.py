def first_action(first_letter, number):
    if first_letter.isupper():
        return number/(ord(first_letter) - 64)
    else:
        return number * (ord(first_letter) - 96)


def second_action(second_letter, number):
    if second_letter.isupper():
        return number - (ord(second_letter) - 64)
    else:
        return number + (ord(second_letter) - 96)


texts = input().split()
results = []
for item in texts:
    first_letter, number, second_letter = item[0], int(item[1:-1]), item[-1]
    result = first_action(first_letter, number)
    result = second_action(second_letter, result)
    results.append(result)

print(f"{sum(results):.2f}")
