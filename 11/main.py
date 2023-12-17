from aoc_meta import *
aoc_init(2023, 11)


data = [[letter == "#" for letter in line] for line in get_input().split("\n")]

import itertools as it

new_data = []
for line in data:
    if all([not cell for cell in line]):
        new_data.append(line)
    new_data.append(line)

data = zip(*new_data[::-1])
new_data = []
for line in data:
    if all([not cell for cell in line]):
        new_data.append(line)
    new_data.append(line)

data = zip(*new_data)

coords = []
for i, line in enumerate(data):
    for j, cell in enumerate(line):
        if cell:
            coords.append((i, j))
        
total = 0
for perm in it.combinations(coords, 2):
    total += sum(map(abs, [perm[0][0] - perm[1][0], perm[0][1] - perm[1][1]]))

print(total)