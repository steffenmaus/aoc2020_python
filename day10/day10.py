with open('input.txt') as file:
    lines = [int(line.rstrip()) for line in file]

lines.append(max(lines) + 3)
lines.append(0)
lines = sorted(lines)

c1 = 0
c3 = 0
last = 0
for c in lines:
    d = c - last
    if d == 1:
        c1 += 1
    elif d == 3:
        c3 += 1
    last = c
print("Part 1: " + str(c1 * c3))

sol = {}


def f(idx):
    idx_max = len(lines) - 1

    if idx in sol:
        return sol[idx]

    if idx == idx_max:
        sol[idx] = 1
        return 1

    count = 0
    for offset in range(1, 4):
        if idx + offset <= idx_max and lines[idx + offset] <= lines[idx] + 3:
            count += f(idx + offset)

    sol[idx] = count
    return count


print("Part 2: " + str(f(0)))
