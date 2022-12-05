#!/usr/bin/env/ python3

curr = 0
maxi = 0
maxis = [0, 0, 0]

with open("inputs/input1.txt") as f:
    for line in f:
        if(line == '\n'):
            if curr > maxi:
                maxi = curr
            if curr > min(maxis):
                maxis[maxis.index(min(maxis))] = curr
            curr = 0
        else:
            curr += int(line)

print(maxi)
print(sum(maxis))
