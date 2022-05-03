from collections import deque

quantity = int(input())
orders_l = [int(i) for i in input().split()]
orders = deque(orders_l)
print(max(orders))

while orders:
    if orders[0] < quantity:
        quantity -= orders.popleft()
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    left = 0
    while orders:
        left += orders.popleft()
    print(f"Orders left: {left}")