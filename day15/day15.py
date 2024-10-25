def f(seed, duration):
    last_spoken = {}
    for k, v in enumerate(seed[:-1]):
        last_spoken[v] = k
    head = seed[-1]
    i = len(seed) - 1
    while i < duration - 1:
        lastpos = last_spoken.get(head, i)
        last_spoken[head] = i
        head = i - lastpos
        i += 1
    return head


spoken = [12, 1, 16, 3, 11, 0]

p1 = f(spoken, 2020)
p2 = f(spoken, 30000000)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
