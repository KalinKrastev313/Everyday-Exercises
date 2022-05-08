
s = []
balance = True

par_o = ["{", "[", "("]
par_cl = {')': "(", ']': "[", '}': "{"}
text = input()

for ch in text:
    if ch in par_o:
        s.append(ch)
    elif ch in par_cl:
        if par_cl[ch] == s[-1]:
            s.pop()
        else:
            balance = False
            break

if s:
    balance = False

if balance:
    print("YES")
else:
    print("NO")