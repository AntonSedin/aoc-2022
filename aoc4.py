#!/usr/bin/env/ python3

fcs = 0
overlaps = 0
with open("inputs/input4.txt") as f:
    for line in f:
        ranges = list(map(int, line.strip().replace('-', ',').split(',')))
        set1 = set(range(ranges[0], ranges[1]+1))
        set2 = set(range(ranges[2], ranges[3]+1))
        if set1.issubset(set2) or set2.issubset(set1):
            fcs += 1
        if set1.intersection(set2):
            overlaps += 1

print(fcs)
print(overlaps)
