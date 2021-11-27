import math
party_size = int(input())
duration = int(input())
coins = 0

for day in range (1, duration +1, 1):
    coins += 50
    coins -= 2*party_size

    if day % 10 == 0:
        party_size -= 2

    if day % 15 == 0:
        party_size += 5

    if day % 3 == 0:
        coins -= 3*party_size

    if day % 5 == 0:
        coins += 20*party_size
        if day % 3 == 0:
            coins -= 2*party_size

print(coins)
coins_per_participant = coins/party_size
coins_per_participant = math.floor(coins_per_participant)
print(f"{party_size} companions received {coins_per_participant} coins each")