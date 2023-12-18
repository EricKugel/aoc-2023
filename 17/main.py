from aoc_meta import *
aoc_init(2023, 17)

import heapq

from collections import namedtuple
Node = namedtuple("Node", ["coords", "heat_loss", "d", "size"])

edges = [list(map(int, line)) for line in get_input().split("\n")]
# edges = [list(map(int, line)) for line in get_test_input().split("\n")]
shape = (len(edges), len(edges[0]))
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# heat loss, direction, size
# vertices = [[Node((row, col), 1000000, 0, 0) for col in range(shape[0])] for row in range(shape[1])]
unexplored = set()
# for row in vertices:
#     unexplored |= set(map(lambda node : node.coords, row))
# vertices[0][0] = Node((0, 0), 0, 1)
goal = (shape[0] - 1, shape[1] - 1)

explored = set()
queue = [Node((0, 0), 0, 1, 0), Node((0, 0), 0, 0, 0)]
while queue:
    node = heapq.heappop(queue)
    if (node.coords, node.d, node.size) in explored:
        continue
    explored |= {(node.coords, node.d, node.size)}
    if node.coords == goal:
        print(node.heat_loss + 1)
        break

    for delta_d in [-1, 0, 1]:
        d = (node.d + delta_d) % 4
        new_coords = (node.coords[0] + directions[d][0], node.coords[1] + directions[d][1])
        if not (0 <= new_coords[0] < shape[0] and 0 <= new_coords[1] < shape[1]):
            continue
        if delta_d == 0 and node.size < 3:
            heapq.heappush(queue, Node(new_coords, node.heat_loss + edges[node.coords[0]][node.coords[1]], d, node.size + 1))
        elif delta_d != 0:
            heapq.heappush(queue, Node(new_coords, node.heat_loss + edges[node.coords[0]][node.coords[1]], d, 1))

# while goal in unexplored:
    
#     unexplored.remove(min_coords)
#     for delta_d in [-1, 1]:
#         new_d = (node.d + delta_d) % 4
#         crossed = []
#         for magnitude in range(1, 4):
#             new_coords = (node.coords[0] + directions[new_d][0] * magnitude, node.coords[1] + directions[new_d][1] * magnitude)
#             crossed.append(new_coords)
#             if not (0 <= new_coords[0] < shape[0] and 0 <= new_coords[1] < shape[1]):
#                 continue
#             new_size = 0 if new_d != node.d else node.size + 1
#             new_heat_loss = node.heat_loss + sum([edges[thing[0]][thing[1]] for thing in crossed])
#             if vertices[new_coords[0]][new_coords[1]].heat_loss > new_heat_loss:
#                 vertices[new_coords[0]][new_coords[1]] = Node(new_coords, new_heat_loss, new_d)

# queue = {paths[0][0]}
# while queue:
#     node = queue.pop()
#     for delta_d in range(-1, 2):
#         new_d = (node.d + delta_d) % 4
#         new_coords = (node.coords[0] + directions[new_d][0], node.coords[1] + directions[new_d][1])
#         if not (0 <= new_coords[0] < shape[0] and 0 <= new_coords[1] < shape[1]):
#             continue
#         new_size = 1 if new_d != node.d else node.size + 1
#         new_heat_loss = node.heat_loss + cost[new_coords[0]][new_coords[1]]
#         if new_size == 3:
#             continue
#         if (new_node := paths[new_coords[0]][new_coords[1]]).heat_loss == 0 or new_node.heat_loss > new_heat_loss or (new_node.heat_loss == new_heat_loss and new_node.size > new_size):
#             paths[new_coords[0]][new_coords[1]] = Node(new_coords, new_heat_loss, new_d, new_size)
#             paths[node.coords[0]][node.coords[1]] = Node(node.coords, node.heat_loss, new_d, 0)
#             queue |= {paths[new_coords[0]][new_coords[1]]}

# output = [list("".join(map(str, line))) for line in cost]
# node = paths[0][0]
# while node != paths[goal[0]][goal[1]]:
#     output[node.coords[0]][node.coords[1]] = ">v<^"[node.d]
#     node = paths[node.coords[0] + directions[node.d][0]][node.coords[1] + directions[node.d][1]]
# print("\n".join(map("".join, paths)), "\n\n")

# print(vertices[goal[0]][goal[1]].heat_loss)