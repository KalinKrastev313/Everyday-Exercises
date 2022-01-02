current_version_str = input().split(".")
current_version = [int(item) for item in current_version_str]
current_version[len(current_version) -1] += 1
for size in range(len(current_version) -1, -1, -1):
    if current_version[size] == 10:
        current_version[size] = 0
        current_version[size - 1] += 1

current_version = [str(item) for item in current_version]
print(".".join(current_version))