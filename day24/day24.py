from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_nei(p):
    x, y = p
    out = []
    for dx, dy in ((2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)):
        out.append((x + dx, y + dy))
    return out


flipped = defaultdict(int)
for l in lines:
    x, y = 0, 0
    rest = l
    while rest:
        if rest.startswith("e"):
            rest = rest[1:]
            x += 2
            y += 0
        elif rest.startswith("se"):
            x += 1
            y += 1
            rest = rest[2:]
        elif rest.startswith("sw"):
            x += -1
            y += 1
            rest = rest[2:]
        elif rest.startswith("w"):
            x += -2
            y += 0
            rest = rest[1:]
        elif rest.startswith("nw"):
            x += -1
            y += -1
            rest = rest[2:]
        elif rest.startswith("ne"):
            x += 1
            y += -1
            rest = rest[2:]
    flipped[(x, y)] += 1

black = [x for x in flipped if flipped[x] % 2 == 1]

p1 = len(black)

for i in range(100):
    all_tiles = set()
    for p in black:
        all_tiles.add(p)
        for q in get_nei(p):
            all_tiles.add(q)

    new_black = set()
    for p in all_tiles:
        black_nei_count = [n in black for n in get_nei(p)].count(True)
        if p in black:
            if black_nei_count in (1, 2):
                new_black.add(p)
        else:
            if black_nei_count == 2:
                new_black.add(p)

    black = new_black

p2 = len(black)
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
