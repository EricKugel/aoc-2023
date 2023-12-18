from aoc_meta import *
aoc_init(2023, 17)

from collections import namedtuple
Node = namedtuple("Node", ["coords", "heat_loss", "d", "size"])

# cost = [list(map(int, line)) for line in get_input().split("\n")]
cost = [list(map(int, line)) for line in get_test_input().split("\n")]
shape = (len(cost), len(cost[0]))

# heat loss, direction, size
paths = [[Node((row, col), 0, 0, 0) for col in range(shape[0])] for row in range(shape[1])]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
goal = (shape[0] - 1, shape[1] - 1)

paths[0][0] = Node((0, 0), 0, 0, -1)
queue = {paths[0][0]}
while queue:
    node = queue.pop()
    for delta_d in range(-1, 2):
        new_d = (node.d + delta_d) % 4
        new_coords = (node.coords[0] + directions[new_d][0], node.coords[1] + directions[new_d][1])
        if not (0 <= new_coords[0] < shape[0] and 0 <= new_coords[1] < shape[1]):
            continue
        new_size = 0 if new_d != node.d else node.size + 1
        new_heat_loss = node.heat_loss + cost[new_coords[0]][new_coords[1]]
        if new_size == 3:
            continue
        if (new_node := paths[new_coords[0]][new_coords[1]]).heat_loss == 0 or new_node.heat_loss > new_heat_loss or (new_node.heat_loss == new_heat_loss and new_node.size > new_size):
            paths[new_coords[0]][new_coords[1]] = Node(new_coords, new_heat_loss, new_d, new_size)
            queue |= {paths[new_coords[0]][new_coords[1]]}

# output = [list("".join(map(str, line))) for line in cost]
# node = paths[0][0]
# while node != paths[goal[0]][goal[1]]:
#     output[node.coords[0]][node.coords[1]] = ">v<^"[node.d]
#     node = paths[node.coords[0] + directions[node.d][0]][node.coords[1] + directions[node.d][1]]
# print("\n".join(map("".join, paths)), "\n\n")

print(paths[goal[0]][goal[1]].heat_loss)