class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @staticmethod
    def can_add_items(items, capacity):
        total_items = sum(value for value in items.values())
        return total_items == capacity

    @staticmethod
    def can_remove_amount(items, item_name, amount):
        if item_name in items and items[item_name] - amount >= 0:
            return True

    @classmethod
    def from_size (cls, name, type, size):
        return cls(name, type, size // 2)

    def remove_item(self, item_name, amount):
        if not self.can_remove_amount(self.items, item_name, amount):
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the store"

    def add_item(self, item_name):
        if self.can_add_items(self.items, self.capacity):
            return "Not enough capacity in the store"

        if not item_name in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the store"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
