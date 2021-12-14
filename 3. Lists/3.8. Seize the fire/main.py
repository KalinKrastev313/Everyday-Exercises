high_range = range(81, 125)
medium_range = range(51, 81)
low_range = range(1, 51)
cells_data = input().split("#")
water = int(input())
effort = 0
completed_cells = []
for cell in range(0, len(cells_data)):
    type_of_fire, value_of_cell = cells_data[cell].split(" = ")
    value_of_cell = int(value_of_cell)
    if not water >= value_of_cell:
        continue
    if type_of_fire == "High" and value_of_cell in high_range:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        completed_cells.append(value_of_cell)
        continue
    if type_of_fire == "Medium" and value_of_cell in medium_range:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        completed_cells.append(value_of_cell)
        continue
    if type_of_fire == "Low" and value_of_cell in low_range:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        completed_cells.append(value_of_cell)
        continue
print("Cells: ")
for item in completed_cells:
    print(f" - {item}")
print(f"Effort: {effort}")
print(f"Total fire: {sum(completed_cells)}")