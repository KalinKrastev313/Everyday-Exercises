clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
items = input().split("|")
budget = int(input())
new_prices = []
profit = 0

for item in items:
    type_item, old_price = item.split("- >")
    old_price = float(old_price)
    if old_price <= budget:
        if type_item == "Clothes" and old_price <= clothes_max_price:
            budget -= old_price
            new_prices.append((old_price * 1.40))
            profit += old_price * 0.4
        if type_item == "Shoes" and old_price <= shoes_max_price:
            budget -= old_price
            new_prices.append((old_price * 1.40))
            profit += old_price * 0.4
        if type_item == "Accessories" and old_price <= accessories_max_price:
            budget -= old_price
            new_prices.append((old_price * 1.40))
            profit += old_price * 0.4

for item in new_prices:
    print(f"{item:.2f}", end = " ")
print(f"\nProfit: {profit:.2f}")
if budget + sum(new_prices) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")