with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

def f(lines, idx_swap):
    idx_visited = set()
    idx = 0
    acc = 0

    while idx not in idx_visited:
        if idx not in range(len(lines)):
            return (False, acc)
        idx_visited.add(idx)
        op = lines[idx].split(" ")[0]
        nu = int(lines[idx].split(" ")[1])
        if idx == idx_swap:
            op = "jmp" if op == "nop" else "nop"
        match op:
            case "nop":
                idx += 1
            case "acc":
                acc += nu
                idx += 1
            case "jmp":
                idx += nu
    return (True, acc)

print("Part 1: " + str(f(lines, -1)[1]))

for i in range(len(lines)):
    r = f(lines, i)
    if not r[0]:
        print("Part 2: " + str(r[1]))
