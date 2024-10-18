import math
import sys

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def extended_euclid(a, b):
    if a == 0:
        return 0, 1
    x, y = extended_euclid(b % a, a)
    return y - (b // a) * x, x


arrival = int(lines[0])
busses = lines[1].split(',')

best = (None, sys.maxsize)
for b in busses:
    if b != 'x':
        b = int(b)
        cycles = math.ceil(arrival / b)
        dep = cycles * b
        if dep < best[1]:
            best = (b, dep)

p1 = best[0] * (best[1] - arrival)
print("Part 1: " + str(p1))

# regular mod operations:
# (a - b) mod m == 0  <==> a mod m == b mod m
# ==> (t+idx)%m==0 ==> t == -idx (mod m)

# chinese remainder theorem:
# For
# x == a1 (mod n1)
# ...
# x == ai (mod ni)
# There is:
# x = sum {ai*Mi*Ni} for i in [1 to k]
# With
# Ni = N/ni be the product of all moduli but one
# Mi and mi such that Mi*Ni + mi*ni == 1

# extended euclidean algorithm:
# solves ax + by = gcd(a,b)
# in case of primes: gcd(p1,p2) == 1


N = 1
for b in busses:
    if b != 'x':
        N *= int(b)

p2 = 0
for i, b in enumerate(busses):
    if b != 'x':
        ni = int(b)
        ai = (ni - i) % ni
        Ni = N // ni
        Mi, mi = extended_euclid(Ni, ni)
        p2 += ai * Mi * Ni

p2 %= N
print("Part 2: " + str(p2))
