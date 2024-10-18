with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

mask = ''
mem = {}
for l in lines:
    if l.startswith('mask'):
        mask = l.split()[-1]
    else:
        pos = l.split('[')[1].split(']')[0]
        end = l.split()[-1]
        bits = bin(int(end))[2:].zfill(36)
        n = 0
        for i in range(0, 36):
            if mask[i] == 'X':
                if bits[i] == '1':
                    n += 2 ** (35 - i)
            elif mask[i] == '1':
                n += 2 ** (35 - i)
        mem[pos] = n

p1 = 0
for m in mem:
    p1 += mem[m]
print("Part 1: " + str(p1))


def f(pool, mask, value, pos):
    if (pos > 35):
        return pool
    out = []
    for c in pool:
        temp = c
        if mask[pos] == 'X':
            out.append(temp + '0')
            out.append(temp + '1')
        elif mask[pos] == '1':
            out.append(temp + '1')
        else:
            out.append(temp + value[pos])
    return f(out, mask, value, pos + 1)


mem = {}
mask = ''
for l in lines:
    if l.startswith('mask'):
        mask = l.split()[-1]
    else:
        pos = l.split('[')[1].split(']')[0]
        pos_bits = bin(int(pos))[2:].zfill(36)
        end = l.split()[-1]
        out = f([''], mask, pos_bits, 0)
        for c in out:
            mem[c] = int(end)

p2 = 0
for m in mem:
    p2 += mem[m]
print("Part 2: " + str(p2))
