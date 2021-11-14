current_year = int(input())
current_year = current_year - 1
result = ""

while result == "":
    current_year = int(current_year)
    current_year = current_year + 1
    current_year = str(current_year)

    for first_index in range (0, len(current_year) - 2, 1):
        if result != "":
            break
        for second_index in range (len(current_year)-1, first_index + 1,-1):
            if result != "" :
                break
            elif current_year[first_index] == current_year[second_index]:
                result = current_year
                break

print(result)