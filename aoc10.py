#!/usr/bin/env/ python3

x = 1
log = [x]
with open("inputs/input10.txt") as f:
    for line in f.readlines():
        command = line.strip().split()
        if command[0] == 'noop':
            log.append(x)
        else:
            log.append(x)
            x += int(command[1])
            log.append(x)

sigsum = 0
for i in range(20, 240, 40):
    sigsum += i * log[i-1]

print(sigsum)

img = ""
for cyc in range(240):
    x = log[cyc]
    if cyc % 40 in [x-1, x, x+1]:
        img += '#'
    else:
        img += '.'
    if cyc % 40 == 39:
        img += '\n'

print()
print(img)
