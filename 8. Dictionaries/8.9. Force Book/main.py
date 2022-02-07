message = input()
users = {}

while not message == "Lumpawaroo":
    if "|" in message:
        side, user = message.split(" | ")
        if side in user:
            users[side].append(user)
        else:
            users[side] = [user]
    else:
        user, side = message.split(" -> ")
        for alliance in users:
            if user in users[alliance]:
                users[alliance].pop(users[alliance].index(user))
                break
        users[side].append(user)
        print(f"{user} joins the {side} side!")

    message = input()


users = dict(sorted(users.items(), key = lambda x: x[0], reverse = False))
users = dict(sorted(users.items(), key = lambda x: len(x[1]), reverse=True))

for side in users:
    if len(users[side]) > 0:
        print(f"Side: {side}, Members: {len(users[side])}")
        users[side] = sorted(users[side])
        for user in users[side]:
            print(f"! {user}")