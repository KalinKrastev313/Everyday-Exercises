Solution of the following exercise: 

Account
Create a class called Account. Upon initialization it should receive id (number), name (string), balance (number; optional; 0 by default). The class should also have 3 instance methods:
credit(amount) - add the amount to the balance and return the new balance
debit(amount) - if the amount is less than or equal to the balance, reduce the balance by the amount and return the new balance. Otherwise return "Amount exceeded balance"
info() - returns "User {name} with account {id} has {balance} balance"
Examples
Test Code	
account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())	

Output
1500
0
User George with account 1234 has 0 balance

Test Code
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())	

Output
Amount exceeded balance
1000
500
User Peter with account 5411256 has 500 balance



