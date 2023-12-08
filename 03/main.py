from aoc_meta import *
aoc_init(2023, 3)

data = list(map(list, get_input().split("\n")))
directions = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1)]

gears = {}

def adjacent(coords):
    for d in directions:
        new_coords = (coords[0] + d[0], coords[1] + d[1])
        if new_coords[0] < 0 or new_coords[0] >= len(data) or new_coords[1] < 0 or new_coords[1] >= len(data[0]):
            continue
        if (symbol := data[new_coords[0]][new_coords[1]]) not in "1234567890.":
            if symbol == "*":
                return True, new_coords
            return True, None
    return False, None

total = 0
for row, line in enumerate(data):
    i = 0
    while i < len(line):
        if (char := line[i]) in "1234567890":
            adj = adjacent((row, i))
            num = char
            i += 1
            while i < len(line) and line[i] in "1234567890":
                num += line[i]
                if not adj[0]:
                    adj = adjacent((row, i))
                i += 1
            if adj[0]:
                if adj[1]:
                    if adj[1] in gears.keys():
                        gears[adj[1]].append(int(num))
                    else:
                        gears[adj[1]] = [int(num)]
        else:
            i += 1

for gear in gears.values():
    if len(gear) == 2:
        total += gear[0] * gear[1]

p2(total)

            