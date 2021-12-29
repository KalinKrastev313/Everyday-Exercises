first_list = input().split(", ")
second_list = input().split(", ")
result_list = []
for item in first_list:
    for i in second_list:
        if item in i:
            result_list.append(item)
            break

print(result_list)