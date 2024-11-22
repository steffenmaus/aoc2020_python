with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def line_parse(l):
    left, right = l.split("(contains ")
    left = left.split()
    right = [x.strip() for x in right.split(")")[0].split(",")]
    return (left, right)


ingredients = set()
allergens = set()
candidates = {}

for l in lines:
    left, right = line_parse(l)
    for temp in right:
        allergens.add(temp.strip())
    for temp in left:
        ingredients.add(temp)

for a in allergens:
    candidates[a] = set()
    for l in lines:
        left, right = line_parse(l)
        if a in right:
            for temp in left:
                candidates[a].add(temp)

for a in allergens:
    for l in lines:
        left, right = line_parse(l)
        if a in right:
            mem = set()
            for temp in candidates[a]:
                if temp not in left:
                    mem.add(temp)
            for m in mem:
                candidates[a].remove(m)

completed = set()
sol = {}
affected = set()
while len(completed) != len(candidates):
    for a in allergens:
        if a not in completed:
            if len(candidates[a]) == 1:
                completed.add(a)
                temp = candidates[a].pop()
                sol[a] = temp
                affected.add(temp)
                for b in allergens:
                    if a != b and b not in completed and temp in candidates[b]:
                        candidates[b].remove(temp)
            elif len(candidates[a]) == 0:
                completed.add(a)

p1 = 0
for i in ingredients:
    if i not in affected:
        for l in lines:
            left, right = line_parse(l)
            if i in left:
                p1 += 1

p2 = ""
for a in sorted(list(allergens)):
    p2 = p2 + sol[a] + ','
p2 = p2[:-1]

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
