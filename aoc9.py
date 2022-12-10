#!/usr/bin/env/ python3

knots = [[0,0] for i in range(10)]
unit = {'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0)}
visited1 = set()
visited2 = set()

with open("inputs/input9.txt") as f:
    for line in f.readlines():
        direc, steps = line.strip().split()
        for _ in range(int(steps)):
            step = unit[direc]
            knots[0][0] += unit[direc][0]
            knots[0][1] += unit[direc][1]
            for i in range(1, len(knots)):
                if (abs(knots[i-1][0] - knots[i][0]) == 2
                and abs(knots[i-1][1] - knots[i][1]) == 2):
                    knots[i][0] += (knots[i-1][0] - knots[i][0]) // 2
                    knots[i][1] += (knots[i-1][1] - knots[i][1]) // 2
                elif knots[i-1][0] - knots[i][0] > 1:
                    knots[i][0] += 1
                    knots[i][1] = knots[i-1][1]
                elif knots[i-1][0] - knots[i][0] < -1:
                    knots[i][0] -= 1
                    knots[i][1] = knots[i-1][1]
                elif knots[i-1][1] - knots[i][1] > 1:
                    knots[i][1] += 1
                    knots[i][0] = knots[i-1][0]
                elif knots[i-1][1] - knots[i][1] < -1:
                    knots[i][1] -= 1
                    knots[i][0] = knots[i-1][0]
                else:
                    break

            visited1.add(tuple(knots[1]))
            visited2.add(tuple(knots[9]))

print(len(visited1))
print(len(visited2))
