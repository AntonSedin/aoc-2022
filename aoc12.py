#!/usr/bin/env/ python3

emap = []

with open("inputs/input12.txt") as f:
    for i, line in enumerate(f.readlines()):
        if 'S' in line:
            start = (i, line.find('S'))
        if 'E' in line:
            end = (i, line.find('E'))

        emap.append([ord(c) for c in line.strip()])

emap[start[0]][start[1]] = ord('a')
emap[end[0]][end[1]] = ord('z')

def neighbors(i, j):
    if i+1 < len(emap):
        yield (i+1, j)
    if i-1 >= 0:
        yield (i-1, j)
    if j+1 < len(emap[0]):
        yield (i, j+1)
    if j-1 >= 0:
        yield (i, j-1)

def print_map():
    for i, row in enumerate(emap):
        for j, x in enumerate(row):
            if (i, j) in visited:
                print(".", end='')
            elif (i, j) in checking:
                print(chr(x).upper(), end='')
            else:
                print(chr(x), end='')
        print()

visited = set()
checking = {start}
steps = 0

while end not in checking:
    #print_map()
    #input()
    to_check = set()
    for i, j in checking:
        visited.add((i, j))
        for x, y in neighbors(i, j):
            if emap[x][y] - emap[i][j] <= 1 and (x, y) not in visited:
                to_check.add((x, y))
    steps += 1
    checking = to_check

print(steps)

visited = set()
checking = {end}
steps = 0

while ord('a') not in [emap[i][j] for i, j in checking]:
    #print_map()
    #input()
    to_check = set()
    for i, j in checking:
        visited.add((i, j))
        for x, y in neighbors(i, j):
            if emap[x][y] - emap[i][j] >= -1 and (x, y) not in visited:
                to_check.add((x, y))
    steps += 1
    checking = to_check

print(steps)

