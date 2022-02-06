company = {}
command = input()

while not command == "End":
    company_name, employee_id = command.split(" -> ")
    if company_name in company:
        if not employee_id in company[company_name]:
            company[company_name].append(employee_id)
    else:
        company[company_name] = [employee_id]

    command = input()

company = dict(sorted(company.items(), key = lambda x: x[0]))

for company_name in company:
    print(f"{company_name}")
    for id in company[company_name]:
        print(f"-- {id}")