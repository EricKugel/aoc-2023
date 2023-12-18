from aoc_meta import *
aoc_init(2023, 17)

import heapq

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Node:
    def __init__(self, coords, heat_loss, d, size):
        self.heat_loss = heat_loss
        self.coords = coords
        self.d = d
        self.size = size
        self.key = (self.coords, self.d, self.size)
    def __lt__(self, other):
        return (self.heat_loss, self.size) < (other.heat_loss, other.size)

grid = {}
for i, row in enumerate(get_input().split("\n")):
# for i, row in enumerate(get_test_input().split("\n")):
    for j, value in enumerate(row):
        grid[(i, j)] = int(value)
shape = (len(get_input().split("\n")), len(get_input().split("\n")[0]))
# shape = (len(get_test_input().split("\n")), len(get_test_input().split("\n")[0]))
goal = (shape[0] - 1, shape[1] - 1)

explored = set()
queue = [Node((0, 0), 0, 0, 0), Node((0, 0), 0, 1, 0)]
while queue:
    node = heapq.heappop(queue)
    if node.key in explored:
        continue
    explored |= {node.key}
    heat_loss, coords, d, size = node.heat_loss, *node.key
    if coords == goal and size >= 4:
        p2(heat_loss)
        break
    if (new_coords := (coords[0] + directions[d][0], coords[1] + directions[d][1])) in grid:
        if (size < 10):
            heapq.heappush(queue, Node(new_coords, heat_loss + grid[new_coords], d, size + 1))
    if size >= 4:
        for d in [(d - 1) % 4, (d + 1) % 4]:
            if (new_coords := (coords[0] + directions[d][0], coords[1] + directions[d][1])) in grid:
                heapq.heappush(queue, Node(new_coords, heat_loss + grid[new_coords], d, 1))
