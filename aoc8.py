#!/usr/bin/env/ python3

with open("inputs/input8.txt") as f:
    rows = [[int(i) for i in line.strip()] for line in f.readlines()]

visible = set()
for i, row in enumerate(rows):
    visible.add((i, 0))
    visible.add((i, len(rows[i]) - 1))
    top = max(row)
    currmax = row[0]
    for j, tree in enumerate(row):
        if tree == top:
            visible.add((i,j))
            break
        if tree > currmax:
            currmax = tree
            visible.add((i,j))
    currmax = row[-1]
    for j, tree in reversed(list(enumerate(row))):
        if tree == top:
            visible.add((i,j))
            break
        if tree > currmax:
            currmax = tree
            visible.add((i,j))

for j, _ in enumerate(rows[0]):
    col = [r[j] for r in rows]
    visible.add((0, j))
    visible.add((len(rows) - 1, j))
    top = max(col)
    currmax = col[0]
    for i, tree in enumerate(col):
        if tree == top:
            visible.add((i,j))
            break
        if tree > currmax:
            currmax = tree
            visible.add((i,j))
    currmax = col[-1]
    for i, tree in reversed(list(enumerate(col))):
        if tree == top:
            visible.add((i,j))
            break
        if tree > currmax:
            currmax = tree
            visible.add((i,j))

print(len(visible))

max_scenic = 0
for i, row in enumerate(rows):
    for j, tree in enumerate(rows[i]):
        col = [r[j] for r in rows]
        left = right = up = down = 0
        for t in reversed(row[:j]):
            left += 1
            if tree <= t:
                break
        for t in row[j+1:]:
            right += 1
            if tree <= t:
                break
        for t in col[i+1:]:
            down += 1
            if tree <= t:
                break
        for t in reversed(col[:i]):
            up += 1
            if tree <= t:
                break
        scenic = left * right * up * down
        max_scenic = max(scenic, max_scenic)

print(max_scenic)
