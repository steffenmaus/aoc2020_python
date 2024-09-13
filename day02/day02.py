with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0
for l in lines:
    s = l.split()
    min = int(s[0].split('-')[0])
    max = int(s[0].split('-')[1])
    c = s[1][0]
    password = s[2]
    if min <= password.count(c) <= max:
        p1 += 1
    if (password[min-1] == c) ^ (password[max-1] == c):
        p2 += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
