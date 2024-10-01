with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

x = 0
y = 0
h = 90

for l in lines:
    a = l[0:1]
    b = int(l[1:])
    match a:
        case 'N':
            y += b
        case 'E':
            x += b
        case 'S':
            y -= b
        case 'W':
            x -= b
        case 'L':
            h = (h - b) % 360
        case 'R':
            h = (h + b) % 360
        case 'F':
            match h:
                case 0:
                    y += b
                case 90:
                    x += b
                case 180:
                    y -= b
                case 270:
                    x -= b

dist = abs(x) + abs(y)
print("Part 1: " + str(dist))

x = 10
y = 1
s_x = 0
s_y = 0

for l in lines:
    a = l[0:1]
    b = int(l[1:])
    match a:
        case 'N':
            y += b
        case 'E':
            x += b
        case 'S':
            y -= b
        case 'W':
            x -= b
        case 'L':
            old_x = x
            old_y = y
            match b:
                case 90:
                    x = - old_y
                    y = old_x
                case 180:
                    x = -old_x
                    y = -old_y
                case 270:
                    x = old_y
                    y = -old_x
        case 'R':
            old_x = x
            old_y = y
            match b:
                case 270:
                    x = - old_y
                    y = old_x
                case 180:
                    x = -old_x
                    y = -old_y
                case 90:
                    x = old_y
                    y = -old_x
        case 'F':
            s_x += b * x
            s_y += b * y

dist = abs(s_x) + abs(s_y)
print("Part 2: " + str(dist))
