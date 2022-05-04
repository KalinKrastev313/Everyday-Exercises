s = [int(i) for i in input().split()]
set_size = int(input())

stack_size = 0
stacks = 0
while s:
    if stack_size + s[-1] < set_size:
        stack_size += s.pop()
    elif stack_size + s[-1] == set_size:
        stacks += 1
        stack_size = 0
    else:
        stacks += 1
        stack_size = s.pop()

if stack_size > 0:
    stacks += 1

print(stacks)