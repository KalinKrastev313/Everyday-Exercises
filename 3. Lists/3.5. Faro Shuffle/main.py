cards_order = input().split()
shuffles_to_be_done = int(input())
half = len(cards_order) // 2
shuffles = 0

first_half = []
second_half = []

while shuffles < shuffles_to_be_done:
    for char in range(0, len(cards_order)):
        if char < half:
            first_half.append(cards_order[char])
        else:
            second_half.append(cards_order[char])
    cards_order = []
    for char in range(0, half):
        cards_order.append(first_half[char])
        cards_order.append(second_half[char])
    first_half = []
    second_half = []
    shuffles += 1

print(cards_order)