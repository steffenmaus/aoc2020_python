with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def inner(current):
    splitted = current.split()
    op = None
    res = int(splitted[0])
    for i, _ in enumerate(splitted):
        if i > 0:
            if splitted[i] == "*":
                op = "*"
            elif splitted[i] == "+":
                op = "+"
            else:
                if op == "*":
                    res *= int(splitted[i])
                else:
                    res += int(splitted[i])
    return res


def inner2(current):
    splitted = current.split()
    for k, v in enumerate(splitted):
        if v == "+":
            new = int(splitted[k - 1]) + int(splitted[k + 1])
            splitted[k - 1] = "1"
            splitted[k] = "*"
            splitted[k + 1] = str(new)

    return inner("".join(s + " " for s in splitted))


def f(line, p1):
    last_open = None
    while len(line.split()) > 1:
        if "(" in line:
            for k, v in enumerate(line):
                if v == "(":
                    last_open = k
                elif v == ")":
                    val = inner(line[last_open + 1:k]) if p1 else inner2(line[last_open + 1:k])
                    line = line.replace("(" + line[last_open + 1:k] + ")", str(val))
                    break
        else:
            return inner(line) if p1 else inner2(line)


p1 = 0
p2 = 0

for l in lines:
    p1 += f(l, True)
    p2 += f(l, False)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
