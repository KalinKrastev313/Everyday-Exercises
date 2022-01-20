The script is one possible solution of the following exercise: 

8. * Vehicle
Create a class Vehicle. The __init__ method should receive: type, model, price. You should also set the owner
to None. The class should have the following methods:
 buy(money, owner) - if the person has enough money and the vehicle has no owner, returns:
"Successfully bought a {type}. Change: {change}" and sets the owner to the given one. If the
money is not enough, return: "Sorry, not enough money". If the car already has an owner, return:
"Car already sold"
 sell() - if the car has an owner, set it to None again. Otherwise, return: "Vehicle has no owner"
 __repr__() - returns "{model} {type} is owned by: {owner}" if the vehicle has an owner.
Otherwise, return: "{model} {type} is on sale: {price}"
Example

Test Code Output

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type,
model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)


