courses = {}
command = input()

while not command == "end":
    course_name, student_name = command.split(" : ")
    if course_name in courses:
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]

    command = input()

courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
for course in courses:
    print(f"{course}: {len(courses[course])}")
    courses[course] = sorted(courses[course])
    for name in courses[course]:
        print(f"-- {name}")