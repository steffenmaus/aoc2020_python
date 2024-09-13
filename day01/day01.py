with open('input.txt') as file:
    lines = [int(line.rstrip()) for line in file]

for a in lines:
    for b in lines:
        if a > b:
            if a + b == 2020:
                print("Part 1: " + str(a * b))
        for c in lines:
            if a > b > c:
                if a + b + c == 2020:
                    print("Part 2: " + str(a * b * c))