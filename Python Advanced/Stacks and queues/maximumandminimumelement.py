def maximum(lst_1):
    lst = [i for i in lst_1]
    m = lst.pop()
    while lst:
        if lst[-1] > m:
            m = lst.pop()
        else:
            lst.pop()
    return m

def minimum(lst_1):
    lst = [i for i in lst_1]
    m = lst.pop()
    while lst:
        if lst[-1] < m:
            m = lst.pop()
        else:
            lst.pop()
    return m


n = int(input())
s = []

for num in range(n):
    expr = input()
    if expr[0] == "1":
        el = expr.split()[1]
        s.append(int(el))
    elif expr[0] == "2":
        if len(s) > 0:
            s.pop()
    elif expr[0] == "3":
        print(maximum(s))
    elif expr[0] == "4":
        print(minimum(s))

while len(s) > 1:
    print(f"{s.pop()}, ", end="")
print(s.pop())