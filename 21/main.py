from aoc_meta import *
aoc_init(2023, 21)

import numpy as np

directions = [1, 1j, -1, -1j]
shape = (len(get_input().split("\n")), len(get_input().split("\n")[0]))
# shape = (len(get_test_input().split("\n")), len(get_test_input().split("\n")[0]))

grid = {}
for i, line in enumerate(get_input().split("\n")):
# for i, line in enumerate(get_test_input().split("\n")):
    for j, letter in enumerate(line):
        if letter == "S":
            start = i + j * 1j
            letter = "."
        for r in [-2, -1, 0, 1, 2]:
            for c in [-2, -1, 0, 1, 2]:
                grid[i + (shape[0] * r) + (shape[1] * c * 1j) + j * 1j] = letter

def get_coords(coords):
    new_coords = set()
    for coord in coords:
        for d in directions:
            new_coord = coord + d
            if new_coord not in grid or grid[new_coord] == "#":
                continue
            new_coords.add(new_coord)
    return new_coords

x = [65, 65 + 131, 65 + 131 + 131]
y = []
for steps in x:
    coords = {start}
    for _ in range(steps):
        coords = get_coords(coords)
    y.append(len(coords))
    
curve = np.poly1d(np.polyfit(x, y, 2))
print(curve(26501365))
# p2(curve(26501365))