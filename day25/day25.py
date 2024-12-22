with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def encrypt(loop_size, subject_number):
    return pow(subject_number, loop_size, 20201227)


def f(public_a, public_b):
    i = 0
    while True:
        res = encrypt(i, 7)
        if res == public_a:
            return encrypt(i, public_b)
        if res == public_b:
            return encrypt(i, public_a)
        i += 1


public_card, public_door = list(map(int, lines))

p1 = f(public_door, public_card)
print("Part 1: " + str(p1))
