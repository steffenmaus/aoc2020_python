with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_grid_from_lines(lines):
    rows = []
    for l in lines:
        cols = []
        for c in l:
            cols.append(c)
        rows.append(cols)
    return rows


import copy

grid = get_grid_from_lines(lines)

y_max = len(grid)
x_max = len(grid[0])
changed = True
while changed:
    changed = False
    new_grid = copy.deepcopy(grid)
    for y in range(y_max):
        for x in range(x_max):
            old = grid[y][x]
            ns = []

            xs = [-1, 0, 1]
            ys = [-1, 0, 1]

            for dx in xs:
                for dy in ys:
                    if 0 <= y + dy < y_max and 0 <= x + dx < x_max and not dx == dy == 0:
                        ns.append(grid[y + dy][x + dx])

            if old == 'L':
                if all(n != '#' for n in ns):
                    new_grid[y][x] = '#'
                    changed = True
            elif old == '#':
                if len([n for n in ns if n == '#']) >= 4:
                    new_grid[y][x] = 'L'
                    changed = True
    grid = copy.deepcopy(new_grid)

c = 0
for y in range(y_max):
    for x in range(x_max):
        if grid[y][x] == '#':
            c += 1

print("Part 1: " + str(c))

grid = get_grid_from_lines(lines)

changed = True
while changed:
    changed = False
    new_grid = copy.deepcopy(grid)
    for y in range(y_max):
        for x in range(x_max):
            old = grid[y][x]
            ns = []

            xs = [-1, 0, 1]
            ys = [-1, 0, 1]
            for dx in xs:
                for dy in ys:
                    temp = (y + dy, x + dx)
                    while (0 <= temp[0] < y_max and 0 <= temp[1] < x_max and not dx == dy == 0
                           and grid[temp[0]][temp[1]] == '.'):
                        temp = (temp[0] + dy, temp[1] + dx)
                    if 0 <= temp[0] < y_max and 0 <= temp[1] < x_max and not dx == dy == 0:
                        ns.append(grid[temp[0]][temp[1]])

            if old == 'L':
                if all(n != '#' for n in ns):
                    new_grid[y][x] = '#'
                    changed = True
            elif old == '#':
                if len([n for n in ns if n == '#']) >= 5:
                    new_grid[y][x] = 'L'
                    changed = True
    grid = copy.deepcopy(new_grid)

c = 0
for y in range(y_max):
    for x in range(x_max):
        if grid[y][x] == '#':
            c += 1

print("Part 2: " + str(c))
