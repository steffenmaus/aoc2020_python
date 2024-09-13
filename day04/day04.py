with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

req = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
hex_digits = '0123456789abcdef'
eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

lines.append('')
passports = []
passport = []
for l in lines:
    if l:
        for e in l.split(' '):
            passport.append(e.split(':'))
    else:
        passports.append(passport)
        passport = []

p1 = 0
p2 = 0
for p in passports:
    valid1 = True
    p_keys = [s[0] for s in p]
    for r in req:
        if r not in p_keys:
            valid1 = False
    p1 += valid1
    valid2 = True
    for t in p:
        match t[0]:
            case 'byr':
                if not 1920 <= int(t[1]) <= 2002:
                    valid2 = False
            case 'iyr':
                if not 2010 <= int(t[1]) <= 2020:
                    valid2 = False
            case 'eyr':
                if not 2020 <= int(t[1]) <= 2030:
                    valid2 = False
            case 'hgt':
                if t[1].endswith('cm'):
                    if not 150 <= int(t[1][:-2]) <= 193:
                        valid2 = False
                elif t[1].endswith('in'):
                    if not 59 <= int(t[1][:-2]) <= 76:
                        valid2 = False
                else:
                    valid2 = False
            case 'hcl':
                if not t[1][0] == '#':
                    valid2 = False
                for c in t[1][1:]:
                    if not c in hex_digits:
                        valid2 = False
            case 'ecl':
                if not t[1] in eye_colors:
                    valid2 = False
            case 'pid':
                if not len(t[1]) == 9:
                    valid2 = False
                elif not t[1].isdigit():
                    valid2 = False
                elif not 0 <= int(t[1]) <= 999999999:
                    valid2 = False
    p2 += valid2 and valid1
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
