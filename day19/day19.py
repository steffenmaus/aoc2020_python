from collections import defaultdict

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


# can not be used for part 2, could be removed
def f(id):
    rule = rules[id]
    if "a" in rule:
        return set("a")
    if "b" in rule:
        return set("b")
    out = set()
    for r in rule:
        if len(r) == 1:
            for x in f(r[0]):
                out.add(x)
        else:
            l = f(r[0])
            r = f(r[1])
            for ll in l:
                for rr in r:
                    out.add(ll + rr)
    return out


# could also solve part 2
def matches(id, remaining):
    if remaining is None:
        return []
    rule = rules[id]
    if "a" in rule and remaining.startswith("a"):
        return [remaining[1:]]
    if "b" in rule and remaining.startswith("b"):
        return [remaining[1:]]
    if "a" in rule or "b" in rule:
        return []
    out = []
    for r in rule:
        temp = [remaining]
        for s in r:
            temp2 = []
            for rem in temp:
                for x in matches(s, rem):
                    temp2.append(x)
            temp = temp2
        for x in temp:
            out.append(x)
    return out


rules = defaultdict(list)

for l in get_groups_from_lines(lines)[0]:
    id, right = l.split(":")
    if "a" in right:
        rules[id] = ["a"]
    elif "b" in right:
        rules[id] = ["b"]
    else:
        for r in right.split("|"):
            rules[id].append(r.strip().split(" "))

all_words = f("0")

rules["8"] = [["42"], ["42", "8"]]
rules["11"] = [["42", "31"], ["42", "11", "31"]]

p1 = 0
p2 = 0

for l in get_groups_from_lines(lines)[1]:
    p1 += l in all_words
    p2 += "" in matches("0", l)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
