#!/usr/bin/env/ python3

monkeys = [{"items": [],
            "op": None,
            "test": None,
            "inspected": 0,
            "true": -1,
            "false": -1,
            } for i in range(8)]

modprod = 1
with open("inputs/input11.txt") as f:
    i = 0
    for line in f.readlines():
        line = line.strip().split()
        if not line:
            i += 1
        elif line[1] == "items:":
            monkeys[i]["items"] = [int(i.replace(",", "")) for i in line[2:]]
        elif line[0] == "Operation:":
            lambstring = "lambda old : "
            for s in line[-3:]:
                lambstring += s
            monkeys[i]["op"] = eval(lambstring)
        elif line[0] == "Test:":
            lambstring = "lambda w : # if not w%{} else ¤".format(line[-1])
            modprod *= int(line[-1])
        elif line[1] == "true:":
            lambstring = lambstring.replace('#', line[-1])
        elif line[1] == "false:":
            lambstring = lambstring.replace('¤', line[-1])
            monkeys[i]["test"] = eval(lambstring)

# 1
#for r in range(1, 21):
for r in range(1, 10001):
    for monkey in monkeys:
        while monkey["items"]:
            item = monkey["items"].pop()
            monkey["inspected"] += 1
            item = monkey["op"](item)
            # 1
            #item = item // 3
            item = item % modprod
            sendto = monkey["test"](item)
            monkeys[sendto]["items"].append(item)

mbs = sorted([monkey["inspected"] for monkey in monkeys])
mb = mbs[-1] * mbs[-2]
print(mb)

