with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

seats = []

for line in lines:
    bin = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    dec = int(bin, 2)
    seats.append(dec)

print("Part 1: " + str(max(seats)))

for s in sorted(seats):
    if s + 1 not in seats:
        p2 = s + 1
        break

print("Part 2: " + str(p2))
