#!/usr/bin/env/ python3

def compare(left, right):
    for l, r in zip(left, right):
        if type(l) != type(r):
            l = [l] if type(l) is int else l
            r = [r] if type(r) is int else r
        if isinstance(l, list) or isinstance(r, list):
            ret = compare(l, r)
            if ret is None:
                continue
            return ret
        if l == r:
            continue
        else:
            return l < r
    if len(left) == len(right):
        return None
    return len(left) < len(right)


delim = None
i = 0
indexsum = 0
div2 = [[2]]
i2 = 1
div6 = [[6]]
i6 = 2
with open("inputs/input13.txt") as f:
    while(delim != ''):
        i += 1
        left = eval(f.readline().strip())
        right = eval(f.readline().strip())
        delim = f.readline()
        if compare(left, right):
            indexsum += i
        if compare(left, div2):
            i2 += 1
            i6 += 1
        elif compare(left, div6):
            i6 += 1
        if compare(right, div2):
            i2 += 1
            i6 += 1
        elif compare(right, div6):
            i6 += 1

print(indexsum)
print(i2 * i6)
