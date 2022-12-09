#!/usr/bin/env python3

shape = {"X": 1, "Y": 2, "Z": 3}
# 1
#win = {"A Y", "B Z", "C X"}
#draw = {"A X", "B Y", "C Z"}
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Z", "B": "X", "C": "Y"}
score = 0

with open("inputs/input2.txt") as f:
    for line in f:
        line = line.strip()
        # 1
        #score += shape[line[2]]
        #if line in win:
        #    score += 6
        #elif line in draw:
        #    score += 3
        if line[2] == "Y":
            score += shape[draw[line[0]]]
            score += 3
        elif line[2] == "Z":
            score += shape[win[line[0]]]
            score += 6
        else:
            score += shape[lose[line[0]]]

print(score)
