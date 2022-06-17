lst = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name, score])

n_lowest = 1 #counter
n = 2 #which lowest
lowest_first = sorted(lst, key=lambda x: x[1])
# print(lowest_first)

names = []

for person in range(1, len(lowest_first)):
    if not lowest_first[person][1] == lowest_first[person - 1][1]:
        n_lowest += 1
        if n == n_lowest:
            names.append(lowest_first[person][0])
            for next_person in range(person + 1, len(lowest_first)):
                if lowest_first[next_person][1] == lowest_first[person][1]:
                    names.append(lowest_first[next_person][0])


for human in sorted(names):
    print(human)