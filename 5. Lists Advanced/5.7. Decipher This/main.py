coded_message = input().split()
first_step = []

for item in coded_message:
    first_letter_code = ""
    while item[0].isdigit():
        first_letter_code += item[0]
        item = item[1:]
    new_item = chr(int(first_letter_code)) + item
    first_step.append(new_item)

coded_message = []
for item in first_step:
    new_item = list(item)
    new_item[1], new_item[len(item) -1] = new_item[len(item) -1], new_item[1]
    new_item = "".join(new_item)
    coded_message.append(new_item)

print(coded_message)