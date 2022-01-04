shell_sizes = [2*(n**2) for n in range(1, 10)]

electrons = int(input())
distribution = []

while electrons >= min(shell_sizes):
    distribution.append(min(shell_sizes))
    electrons -= min(shell_sizes)
    shell_sizes.remove(min(shell_sizes))

if not electrons == 0:
    distribution.append(electrons)
print(distribution)