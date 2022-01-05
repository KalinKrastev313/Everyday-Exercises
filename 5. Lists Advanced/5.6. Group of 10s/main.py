numbers_unsorted_str = input().split(", ")
numbers_unsorted_int = [int(number) for number in numbers_unsorted_str]
numbers_sorted = sorted(numbers_unsorted_int)
print(numbers_sorted)
numbers_sorted.append(200)
for boundry in range(10,110, 10):
    group = []

    if len(numbers_sorted) > 1:
        while numbers_sorted[0] <= boundry:
            group.append(numbers_sorted[0])
            numbers_sorted.remove(numbers_sorted[0])
        print(f"Group of {boundry}'s: {group}")