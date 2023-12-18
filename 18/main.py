from aoc_meta import *
aoc_init(2023, 18)

import re

data = get_input().split("\n")
coords = (0, 0)
corners = [coords]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

perimeter = 0
for i, line in enumerate(data):
    d, length, hex = line.split(" ")
    hex = hex[2:-1]
    d = directions[int(hex[-1])]
    length = int(hex[:-1], 16)
    
    coords = (coords[0] + d[0] * length, coords[1] + d[1] * length)
    corners.append(coords)
    perimeter += length
    data[i] = (d, length)
        
top, left = (min(corners, key = lambda corner : corner[0])[0], min(corners, key = lambda corner : corner[1])[1])
area = 0
coords = (0, 0)
for d, length in data:
    if d[0] == 0:
        area += -d[1] * (coords[0] - top) * length
    coords = (coords[0] + d[0] * length, coords[1] + d[1] * length)
area += perimeter // 2 + 1
p2(area)