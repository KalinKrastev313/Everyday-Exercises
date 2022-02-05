students = {}
rounds = int(input())

for n in range(rounds):
    name = input()
    grade = float(input())
    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]

for student in students:
    students[student] = (sum(students[student])/len(students[student]))
    if students[student] < 4.50:
        students[student] = False

students = dict(sorted(students.items(), key = lambda x: x[1], reverse=True))
for name in students:
    if students[name]:
        print(f"{name} -> {(students[name]):.2f}")