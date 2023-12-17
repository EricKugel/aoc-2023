from aoc_meta import *
aoc_init(2023, 11)

data = [[letter == "#" for letter in line] for line in get_input().split("\n")]

value =  1000000 - 1

def get_lines_below(i, data):
    return sum([all([not cell for cell in line]) for line in data[0:i]])

import itertools as it

coords = []
for i, line in enumerate(data):
    for j, cell in enumerate(line):
        if cell:
            coords.append([i, j])

for coord in coords:
    coord[0] += value * get_lines_below(coord[0], data)

data = list(zip(*data))

for coord in coords:
    coord[1] += value * get_lines_below(coord[1], data)

total = 0
for perm in it.combinations(coords, 2):
    total += sum(map(abs, [perm[0][0] - perm[1][0], perm[0][1] - perm[1][1]]))

p2(total)