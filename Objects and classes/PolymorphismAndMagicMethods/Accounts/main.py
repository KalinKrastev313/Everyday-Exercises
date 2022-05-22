class Account:
    def __init__(self, owner, amount=0, transactions=[]):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.__index = -1

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.balance()}"

    def __repr__(self):
        return f"Account({self.owner}, {self.balance()})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self._transactions):
            self.__index = -1
            raise StopIteration
        else:
            return self._transactions[self.__index]

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __gt__(self, other):
        return self.balance() > other.balance()

    def __ge__(self, other):
        return self.balance() >= other.balance()

    def __add__(self, other):
        owners_combined = f"{self.owner}&{other.owner}"
        amounts_combined = self.amount + other.amount
        transactions_combined = self._transactions + other._transactions
        return Account(owners_combined, amounts_combined, transactions_combined)

    def add_transaction(self, amount):
        if not type(amount) == int:
            raise ValueError("please use int for amount")
        else:
            self._transactions.append(amount)

    def balance(self):
        return self.amount + sum(self._transactions)

    def validate_transaction(self, account, amount_to_add):
        if account.balance() - amount_to_add >= 0:
            self._transactions.append(amount_to_add)
            return f"New balance: {self.balance()}"
        else:
            raise ValueError("sorry cannot go in debt!")


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance())
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)




