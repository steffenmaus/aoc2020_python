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

rules = groups[0]
my_ticket = groups[1][1]
nearby_tickets = groups[2][1:]
valid_tickets = []

valid_per_rule = {}
chances_per_rule = {}

all_valid_values = set()
j = 0
for r in rules:
    temp = set()
    r = r.split(":")[1]
    a, _, b = r.split()
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    for i in range(int(a1), int(a2) + 1):
        temp.add(i)
        all_valid_values.add(i)
    for i in range(int(b1), int(b2) + 1):
        temp.add(i)
        all_valid_values.add(i)
    valid_per_rule[j] = temp
    j += 1

p1 = 0
for t in nearby_tickets:
    valid = True
    for v in t.split(','):
        v = int(v)
        if v not in all_valid_values:
            valid = False
            p1 += v
    if valid:
        valid_tickets.append(t)

print("Part 1: " + str(p1))

for i, _ in enumerate(rules):
    possible_pos = set()
    for j, _ in enumerate(rules):
        possible = True
        for t in valid_tickets:
            if not int(t.split(',')[j]) in valid_per_rule[i]:
                possible = False
        if possible:
            possible_pos.add(j)
    chances_per_rule[i] = possible_pos

p2 = 1

completed = 0
while completed < len(rules):
    for i in chances_per_rule:
        if len(chances_per_rule[i]) == 1:
            completed += 1
            e = chances_per_rule[i].pop()
            if rules[i].startswith("departure"):
                p2 *= int(my_ticket.split(',')[e])
            for j in chances_per_rule:
                if e in chances_per_rule[j]:
                    chances_per_rule[j].remove(e)

print("Part 2: " + str(p2))
