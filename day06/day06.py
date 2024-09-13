import string

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


groups = get_groups_from_lines(lines)

p1 = 0
p2 = 0
for g in groups:
    for c in string.ascii_lowercase:
        if any(c in l for l in g):
            p1 += 1
        if all(c in l for l in g):
            p2 += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))