products = {}
price_and_quantity = []
command = input()

while not command == "buy":
    name, price, quantity = command.split()
    price_and_quantity.append(float(price))
    price_and_quantity.append(int(quantity))
    if name in products:
        products[name][0] = price_and_quantity[0]
        products[name][1] += price_and_quantity[1]
    else:
        products[name] = price_and_quantity

    price_and_quantity = []
    command = input()

for (key, value) in products.items():
    print(f"{key} -> {(value[0]*value[1]):.2f}")