#!/usr/bin/env/ python3

priosum = 0
badgepriosum = 0
s = set()
with open("inputs/input3.txt") as f:
    for i, line in enumerate(f):
        line = line.strip()
        mid = len(line)//2
        c = set(line[:mid]).intersection(line[mid:]).pop()
        if c.islower():
            prio = ord(c) - 96
            priosum += prio
        else:
            prio = ord(c) - 38
            priosum += prio
        if i % 3 == 0:
            s = set(line)
        elif i % 3 == 1:
            s = s.intersection(line)
        else:
            c = s.intersection(line).pop()
            if c.islower():
                prio = ord(c) - 96
                badgepriosum += prio
            else:
                prio = ord(c) - 38
                badgepriosum += prio

print(priosum)
print(badgepriosum)
