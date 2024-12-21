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


def calc_score(deck):
    score = 0
    for i, v in enumerate(reversed(deck)):
        score += (i + 1) * v
    return score


def comb(deck1, deck2):
    while deck1 and deck2:
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)
    if deck1:
        return deck1
    else:
        return deck2


def rec_comb(deck1, deck2):
    prev_rounds = set()
    while deck1 and deck2:
        state = str(deck1) + str(deck2)
        if state in prev_rounds:
            return True, deck1
        else:
            prev_rounds.add(state)
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if len(deck1) >= c1 and len(deck2) >= c2:
            if rec_comb(deck1[:c1], deck2[:c2])[0]:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)
        else:
            if c1 > c2:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)
    if deck1:
        return True, deck1
    else:
        return False, deck2


deck1, deck2 = get_groups_from_lines(lines)

deck1.pop(0)
deck2.pop(0)

deck1 = [int(x) for x in deck1]
deck2 = [int(x) for x in deck2]

p1 = calc_score(comb(deck1.copy(), deck2.copy()))
p2 = calc_score(rec_comb(deck1.copy(), deck2.copy())[1])

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
