with open('input.txt') as file:
    grid = [line.rstrip() for line in file]

steps = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

p2 = 1

for s in steps:
    x = 0
    y = 0
    p1 = 0
    while y < len(grid) - 1:
        x += s[0]
        x %= len(grid[0])
        y += s[1]
        p1 += grid[y][x] == '#'
    if s == (3, 1):
        print("Part 1: " + str(p1))
    p2 *= p1

print("Part 2: " + str(p2))
