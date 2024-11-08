with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_n(x, y, z, w):
    out = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                if w is None:
                    if dx != 0 or dy != 0 or dz != 0:
                        out.append((x + dx, y + dy, z + dz))
                else:
                    for dw in (-1, 0, 1):
                        if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                            out.append((x + dx, y + dy, z + dz, w + dw))
    return out


def f(seed, p1):
    X = len(lines[0])
    Y = len(lines)
    active = set()
    if p1:
        for s in seed:
            active.add((s[0], s[1], s[2]))
    else:
        active = seed.copy()
    for i in range(1, 7):
        new_active = set()
        for x in range(0 - i, X + 1 + i):
            for y in range(0 - i, Y + 1 + i):
                for z in range(0 - i, 1 + i):
                    if p1:
                        all_n = get_n(x, y, z, None)
                        act_n = len([p for p in all_n if p in active])
                        if (x, y, z) in active and act_n in (2, 3):
                            new_active.add((x, y, z))
                        elif (x, y, z) not in active and act_n == 3:
                            new_active.add((x, y, z))
                    else:
                        for w in range(0 - i, 1 + i):
                            all_n = get_n(x, y, z, w)
                            act_n = len([p for p in all_n if p in active])
                            if (x, y, z, w) in active and act_n in (2, 3):
                                new_active.add((x, y, z, w))
                            elif (x, y, z, w) not in active and act_n == 3:
                                new_active.add((x, y, z, w))
        active = new_active

    return len(active)


seed = set()
for y, _ in enumerate(lines):
    for x, _ in enumerate(lines[0]):
        if lines[y][x] == '#':
            seed.add((x, y, 0, 0))

p1 = f(seed, True)
p2 = f(seed, False)
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
