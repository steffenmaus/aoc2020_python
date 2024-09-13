with open('input.txt') as file:
    lines = [int(line.rstrip()) for line in file]


def f(lines):
    width = 25
    queue = []
    for i, v in enumerate(lines):
        if i < width:
            queue.append(v)
        else:
            match = False
            for a in queue:
                for b in queue:
                    if a != b and a + b == v:
                        match = True
            if not match:
                return v
            queue.pop(0)
            queue.append(v)


def f2(lines, p):
    i = 0
    j = 1
    v = lines[i] + lines[j]
    while v != p:
        if v < p:
            j += 1
            v += lines[j]
        else:
            v -= lines[i]
            i += 1
    r = lines[i:j+1]
    return max(r) + min(r)


p1 = f(lines)
print("Part 1: " + str(p1))
print("Part 2: " + str(f2(lines, p1)))