class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if money >= self.price and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {self.price - money}"
        elif money <= self.price:
            return "Sorry not enough money"
        elif money >= self.price and not self.owner is None:
            return "Car already sold"

    def sell(self):
        if not self.owner is None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if not self.owner is None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)

# Does not print what is returned, but saves the values right