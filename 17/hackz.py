from aoc_meta import *
aoc_init(2023, 17)

import random

cost = [list(map(int, line)) for line in get_input().split("\n")]
# cost = [list(map(int, line)) for line in get_test_input().split("\n")]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_heat_loss(path):
    return sum([cost[coord[0]][coord[1]] for coord in path])

min_heat_loss = 1000
while True:
    path = []
    coords = (0, 0)
    size = 0
    d = random.choice([0, 1])
    heat_loss = 0
    while coords != (len(cost) - 1, len(cost[0]) - 1):
        delta_d = None
        attempts = 0
        while not delta_d or not ((0 <= new_coords[0] < len(cost) and 0 <= new_coords[1] < len(cost[0])) or new_coords in path or new_size <= 3):
            delta_d = random.choice([-1, 0, 1])
            new_d = (d + delta_d) % 4
            new_coords = (coords[0] + directions[new_d][0], coords[1] + directions[new_d][1])
            new_size = 1 if d == new_d else size + 1
            attempts += 1
            if attempts > 10:
                break
        if attempts > 10:
            heat_loss = min_heat_loss
            break
        coords, size, d = new_coords, new_size, new_d
        path.append(coords)
        heat_loss += cost[coords[0]][coords[1]]
        if heat_loss > min_heat_loss:
            break
    if heat_loss < min_heat_loss:
        min_heat_loss = heat_loss
        print(min_heat_loss)