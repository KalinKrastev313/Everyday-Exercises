directory = input().split('\\')
name, extension = directory[len(directory) -1].split(".")
print(f"File name: {name}\nFile extension: {extension}")