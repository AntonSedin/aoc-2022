#!/usr/bin/env/ python3

i = 3

with open("inputs/input6.txt") as f:
    c = f.read(3)
    marker = [x for x in c]
    while c != '\n':
        c = f.read(1)
        marker.append(c)
        i += 1
        if len(set(marker)) == 4:
            print(i)
            c = f.read(9)
            for x in c:
                marker.append(c)
            i += 9
            while c != '\n':
                c = f.read(1)
                marker.append(c)
                i += 1
                if len(set(marker)) == 14:
                    print(i)
                    quit()
                del marker[0]
        del marker[0]
