#!/usr/bin/env/ python3

setup = True
stacks = [[] for x in range(9)]

with open("inputs/input5.txt") as f:
    for line in f:
        if setup:
            if line == '\n':
                setup = False
                for stack in stacks:
                    stack = stack.reverse()
                continue
            for i, j in enumerate(range(1, 35, 4)):
                c = line[j]
                if c.isdigit() or c == ' ':
                    continue
                stacks[i].append(line[j])
        else:
            line = line.strip()
            [num, fro, to] = [int(x) for x in line.split() if x.isdigit()]
            # 1
            #for _ in range(num):
            #    stacks[to-1].append(stacks[fro-1].pop())
            for box in stacks[fro-1][-num:]:
                stacks[to-1].append(box)
            stacks[fro-1] = stacks[fro-1][:-num]

for stack in stacks:
    print(stack.pop())
