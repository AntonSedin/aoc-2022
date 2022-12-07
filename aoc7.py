#!/usr/bin/env/ pytho

class FSTree:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.size = 0
        self.dirs = []

def traverse(tree):
    yield tree.size
    for child in tree.dirs:
        yield from traverse(child)

def main():
    with open("inputs/input7.txt") as f:
        curr = FSTree(None, "/")
        for line in f.readlines():
            line = line.split()
            if line[0] == "$":
                if line[1] == "ls":
                    continue
                if line[2] == "..":
                    curr = curr.parent
                else:
                    for child in curr.dirs:
                        if child.name == line[2]:
                            curr = child
            elif line[0] == "dir":
                curr.dirs.append(FSTree(curr, line[1]))
            else:
                size = int(line[0])
                curr.size += size
                par = curr.parent
                while par:
                    par.size += size
                    par = par.parent

    while curr.parent:
        curr = curr.parent

    free_space = 70000000 - curr.size
    space_req = 30000000 - free_space

    sum_small = 0
    min_del = 999999999999999
    for size in traverse(curr):
        if size <= 100000:
            sum_small += size
        if space_req <= size <= min_del:
            min_del = size

    print(sum_small)
    print(min_del)

if __name__ == "__main__":
    main()
