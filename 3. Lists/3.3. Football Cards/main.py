A = 11
B = 11
cards = input().split()
game_terminated = False


for index in range(len(cards)):
    if cards[index][0] == "A":
        A = A -1
    else:
        B = B -1
    if A == 6 or B == 6:
        print(f"Team A - {A}; Team B - {B} \nGame was terminated")
        game_terminated = True
        break

if game_terminated == False:
    print(f"Team A - {A}; Team B - {B}")