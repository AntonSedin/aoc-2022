#!/usr/bin/env/ python3

curr = 0
maxi = [0, 0, 0]

with open("inputs/input1.txt") as f:
    for line in f:
        if(line == '\n'):
            if curr > min(maxi):
                maxi[maxi.index(min(maxi))] = curr
            curr = 0
        else:
            curr += int(line)

print(sum(maxi))
