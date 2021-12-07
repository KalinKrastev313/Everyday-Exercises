coins = input().split(", ")
for element in range(len(coins)):
    coins[element] = int(coins[element])
n = int(input())
turn = 0
result = []
previous_addition = 0
result_beggar = 0
for number in range (n):
    if turn < len(coins):
        result_beggar += coins[turn]
    while previous_addition + n + turn < len(coins):
        result_beggar += coins[previous_addition + n + turn]
        previous_addition = previous_addition + n
    result.append(result_beggar)
    turn = turn + 1
    previous_addition = 0
    result_beggar = 0

print(result)