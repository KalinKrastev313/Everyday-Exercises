first_string = input()
first_string += " "
second_string = input()
second_string += " "
result = ""
rest = ""
for number in range (1, len(first_string), 1):
    if first_string[number - 1] != second_string[number - 1]:
        result += second_string[number-1]
        for index in range (number, len(first_string), 1):
            rest += first_string[index]
        print(result + rest)
        rest = ""
    else:
        result += first_string[number-1]