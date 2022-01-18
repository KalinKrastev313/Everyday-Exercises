The script is one possible solution of the following exercise: 

6. Inventory
Create a class Inventory. The __init__ method should accept only the capacity of the inventory. The capacity should
be a private attribute (__capacity). You can read more about private attributes here. Each inventory should also
have an attribute called items, where all the items will be stored. The class should also have 3 methods:
 add_item(item) - adds the item in the inventory if there is space for it. Otherwise, returns
"not enough room in the inventory"
 get_capacity() - returns the value of __capacity
 __repr__() - returns "Items: {items}.\nCapacity left: {left_capacity}". The items should
be separated by ", "
Example

Test Code Output

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

not enough room in the inventory
2
Items: potion, sword.
Capacity left: 0


