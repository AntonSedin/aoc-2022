#!/usr/bin/env/ python3

head = [0, 0]
tail = [0, 0]
visited = set()

with open("inputs/input9.txt") as f:
    for line in f.readlines():
        direc, steps = line.strip().split()
        for _ in range(int(steps)):
            if direc == 'U':
                head[1] += 1
                if abs(head[1] - tail[1]) >= 2:
                    tail[1] += 1
                    tail[0] = head[0]
            elif direc == 'D':
                head[1] -= 1
                if abs(head[1] - tail[1]) >= 2:
                    tail[1] -= 1
                    tail[0] = head[0]
            elif direc == 'L':
                head[0] -= 1
                if abs(head[0] - tail[0]) >= 2:
                    tail[0] -= 1
                    tail[1] = head[1]
            elif direc == 'R':
                head[0] += 1
                if abs(head[0] - tail[0]) >= 2:
                    tail[0] += 1
                    tail[1] = head[1]
            visited.add(tuple(tail))

print(len(visited))
