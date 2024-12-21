class Cup:
    def __init__(self, n):
        self.n = n

    def set_successor(self, cup):
        self.successor = cup

    def drop3(self):
        old_suc = self.successor
        self.successor = self.successor.successor.successor.successor
        return old_suc

    def add3(self, cup):
        old_suc = self.successor
        self.successor = cup
        self.successor.successor.successor.successor = old_suc


def get_initial_cups(part1, seed):
    cups = {}
    prev = None
    for c in seed:
        temp = Cup(c)
        cups[c] = temp
        if prev is not None:
            prev.set_successor(temp)
        prev = temp

    if not part1:
        for i in range(10, 1000001):
            temp = Cup(i)
            cups[i] = temp
            if prev is not None:
                prev.set_successor(temp)
            prev = temp

    first = cups[seed[0]]
    prev.set_successor(first)
    return cups, first


def f(start, cups, times, max):
    current = start
    for i in range(times):
        picked = current.drop3()
        dest_cup = current.n - 1
        while dest_cup == 0 or dest_cup in [picked.n, picked.successor.n, picked.successor.successor.n]:
            dest_cup = (dest_cup - 1) % (max + 1)
        cups[dest_cup].add3(picked)
        current = current.successor


seed = list(map(int, list("496138527")))

cups, first = get_initial_cups(True, seed)
f(first, cups, 100, 9)

p1 = ""
current = cups[1].successor
while current.n != 1:
    p1 += str(current.n)
    current = current.successor

print("Part 1: " + str(p1))

cups, first = get_initial_cups(False, seed)
f(first, cups, 10000000, 1000000)

p2 = cups[1].successor.n * cups[1].successor.successor.n

print("Part 2: " + str(p2))
