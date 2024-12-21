with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_groups_from_lines(lines):
    groups = []
    group = []
    for l in lines:
        if not l:
            groups.append(group)
            group = []
        else:
            group.append(l)
    groups.append(group)
    return groups


def grid_get_from_lines(l):
    return [list(x) for x in l]


def grid_get_flipped_left_right(g):
    return [r[::-1] for r in g]


def grid_get_rotated_r_90(g):
    return [list(x) for x in list(zip(*g[::-1]))]


def grid_get_without_outer_ring(g):
    return [r[1:-1] for r in g[1:-1]]


def get_edge_shapes(grid):  # NESW
    r90 = grid_get_rotated_r_90(grid)
    r180 = grid_get_rotated_r_90(r90)
    r270 = grid_get_rotated_r_90(r180)
    return [grid[0], r270[0], r180[0], r90[0]]


def get_flipped_shape(shape):
    return shape[::-1]


mem = {}


def get_shape(id, flipped, rotation, dir):
    if (id, flipped, rotation, dir) in mem.keys():
        return mem[(id, flipped, rotation, dir)]
    sides = get_edge_shapes(tiles[id])
    if flipped == 0:
        mem[(id, flipped, rotation, dir)] = sides[(dir - rotation) % 4]
    else:
        mem[(id, flipped, rotation, dir)] = get_flipped_shape(sides[-(dir - rotation) % 4])
    return mem[(id, flipped, rotation, dir)]


# bruteforce 12x12 grid with matching edges
def f(state, completed):  # state: [(id, flipped, r90)]
    pos = len(state)
    if pos == 144:
        return state
    x = pos % 12
    y = pos // 12

    if y == 0 and x == 0:
        for id in tiles.keys():
            for flipped in (0, 1):
                for rotation in (0, 1, 2, 3):
                    res = f([(id, flipped, rotation)], {id})
                    if res is not None:
                        return res

    top = None
    left = None
    if x > 0:
        left = state[-1]
    if y > 0:
        top = state[-12]
    for id in tiles.keys():
        if id not in completed:
            for flipped in (0, 1):
                for rotation in (0, 1, 2, 3):
                    if top is None or get_shape(top[0], top[1], top[2], 2) == get_flipped_shape(
                            get_shape(id, flipped, rotation, 0)):
                        if left is None or get_shape(left[0], left[1], left[2], 1) == get_flipped_shape(
                                get_shape(id, flipped, rotation, 3)):
                            res = f(state + [(id, flipped, rotation)], completed.union({id}))
                            if res is not None:
                                return res
    return None


tiles = {}

for g in get_groups_from_lines(lines):
    id = int(g[0].split(":")[0].split(" ")[1])
    tiles[id] = grid_get_from_lines(g[1:])

order = f([], set())
p1 = order[0][0] * order[11][0] * order[-12][0] * order[-1][0]
print("Part 1: " + str(p1))

big_grid = []
for i, e in enumerate(order):
    id, flipped, rotation = e
    xoffset = (i % 12) * 8
    yoffset = (i // 12) * 8

    tempgrid = tiles[id]
    if flipped:
        tempgrid = grid_get_flipped_left_right(tempgrid)
    for _ in range(rotation):
        tempgrid = grid_get_rotated_r_90(tempgrid)

    tempgrid = grid_get_without_outer_ring(tempgrid)
    if i % 12 == 0:
        for l in tempgrid:
            big_grid.append(l)
    else:
        for i, l in enumerate(tempgrid):
            big_grid[-8 + i] = big_grid[-8 + i] + l

nessie = [list("                  # "), list("#    ##    ##    ###"), list(" #  #  #  #  #  #   ")]

p2 = 0
monsters = set()
for flipped in (0, 1):
    for rotated in (0, 1, 2, 3):
        for y in range(96):
            for x in range(96):
                candidates = set()
                valid = True
                for dy in range(len(nessie)):
                    for dx in range(len(nessie[0])):
                        p = (x + dx, y + dy)
                        if valid and 0 <= dx + x < 96 and 0 <= dy + y < 96:
                            if nessie[dy][dx] == "#":
                                candidates.add(p)
                                if big_grid[dy + y][dx + x] != "#":
                                    valid = False
                        else:
                            valid = False
                if valid:
                    for c in candidates:
                        monsters.add(c)
        big_grid = grid_get_rotated_r_90(big_grid)
    big_grid = grid_get_flipped_left_right(big_grid)

p2 = sum(x.count("#") for x in big_grid) - len(monsters)
print("Part 2: " + str(p2))
