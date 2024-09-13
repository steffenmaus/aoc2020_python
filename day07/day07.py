with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

start_bag = "shiny gold"

outer_bags = set()
queue = set()
queue.add(start_bag)
while len(queue) != 0:
    k = queue.pop()
    for l in lines:
        if k in l.split("contain")[1]:
            queue.add(l.split(" bags")[0])
            outer_bags.add(l.split(" bags")[0])
print("Part 1: " + str(len(outer_bags)))

bag_children = {}
for l in lines:
    k = l.split(" bags")[0]
    v = set()
    t = l.split("contain ")[1]
    for x in t.split(", "):
        if x != "no other bags.":
            c = x.split(" bag")[0]
            count = int(c.split(" ")[0])
            type = c.split(" ", 1)[1]
            v.add((type, count))
    bag_children[k] = v


def rec(map, bag):
    if len(map[bag]) == 0:
        return 1
    else:
        c = 0
        for t in map[bag]:
            c += t[1] * rec(map, t[0])
        return 1 + c


print("Part 2: " + str(rec(bag_children, start_bag) - 1))
