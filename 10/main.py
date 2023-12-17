from aoc_meta import *
aoc_init(2023, 10)

from PIL import Image

data = get_input().split("\n")
# data = get_test_input().split("\n")

directions = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1)]

# n (-1, 0)
# e (0, 1)
# s (1, 0)
# w (0, -1)

pipe_types = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    # "S": directions
    "S": [(0, 1), (0, -1)],
}


pipes = {}
class Pipe:
    def __init__(self, coords):
        self.coords = coords
        self.type = data[coords[0]][coords[1]]
        pipes[coords] = self
        self.value = 0
    def get_neighbors(self):
        return [(self.coords[0] + delta[0], self.coords[1] + delta[1]) for delta in pipe_types[self.type]]

for i, line in enumerate(data):
    for j, letter in enumerate(line):
        if letter == "S":
            start = (i, j)
        elif letter == ".":
            continue
        Pipe((i, j))

queue = {start}
visited = {start}
while queue:
    node = queue.pop()
    neighbors = [(node[0] + d[0], node[1] + d[1]) for d in directions]
    neighbors = list(filter(lambda neighbor : neighbor in pipes.keys() and node in pipes[neighbor].get_neighbors() and neighbor in pipes[node].get_neighbors(), neighbors))
    for neighbor in neighbors:
        if neighbor not in visited or pipes[neighbor].value > pipes[node].value + 1:
            visited |= {neighbor}
            pipes[neighbor].value = pipes[node].value + 1
            queue |= {neighbor}


# # Every time you cross a pipe, flip good
# pipes[start].value = 1
# total = 0
# output = ""
# for row in range(len(data)):
#     good = (row, 0) in pipes.keys() and pipes[(row, 0)].value > 0
#     for col in range(1, len(data[0])):
#         if (row, col) in pipes.keys() and (pipe := pipes[(row, col)]).value > 0:
#             if pipe.type == "-":
#                 continue
#             elif pipe.type in "|JL":
#                 good = not good
#             # output += "O" if data[row][col] == "." else data[row][col]
#             output += " "
#         elif good:
#             total += 1
#             output += "I"
#         else: output += " "
#     output += "\n"

# print(output)
# print(total)

pipes[start].value = 1

pipe_shapes = {
    "|": ((0, 1, 0), (0, 1, 0), (0, 1, 0)),
    "-": [(0, 0, 0), (1, 1, 1), (0, 0, 0)],
    "L": [(0, 1, 0), (0, 1, 1), (0, 0, 0)],
    "J": [(0, 1, 0), (1, 1, 0), (0, 0, 0)],
    "7": [(0, 0, 0), (1, 1, 0), (0, 1, 0)],
    "F": [(0, 0, 0), (0, 1, 1), (0, 1, 0)],

    # -
    "S": [(0, 0, 0), (1, 1, 1), (0, 0, 0)]

    # F
    # "S": [(0, 0, 0), (0, 1, 1), (0, 1, 0)]
    # "S": [(0, 1, 0), (1, 1, 0), (0, 0, 0)],
    # "S": [(0, 1, 0), (0, 1, 1), (0, 0, 0)],

    # 7
    # "S": [(0, 0, 0), (1, 1, 0), (0, 1, 0)]
}

new_grid = [[0 for col in range(len(data[0]) * 3)] for row in range(len(data) * 3)]
for row in range(len(data) * 3):
    for col in range(len(data[0]) * 3):
        r, c = row // 3, col // 3
        if (r, c) in pipes.keys() and pipes[(r, c)].value > 0:
            new_grid[row][col] = pipe_shapes[pipes[(r, c)].type][row % 3][col % 3]

new_new_grid = [line.copy() for line in new_grid.copy()]
queue = {(start[0] * 3 + 1, start[1] * 3 + 1)}
visited = {(start[0] * 3 + 1, start[1] * 3 + 1)}
while queue:
    node = queue.pop()
    neighbors = [(node[0] + d[0], node[1] + d[1]) for d in directions]
    neighbors = filter(lambda n : 0 <= n[0] < len(new_grid) and 0 <= n[1]  < len(new_grid[0]), neighbors)
    for neighbor in neighbors:
        if neighbor not in visited and new_grid[neighbor[0]][neighbor[1]]:
            new_new_grid[neighbor[0]][neighbor[1]] = 1
            visited |= {neighbor}
            queue |= {neighbor}

new_grid = new_new_grid

print("\n".join(["".join(["#" if letter else " "for letter in line]) for line in new_grid]))

queue = {(0, 0)}
new_grid[0][0] = 1
while queue:
    node = queue.pop()
    neighbors = [(node[0] + d[0], node[1] + d[1]) for d in directions]
    neighbors = filter(lambda n : 0 <= n[0] < len(new_grid) and 0 <= n[1]  < len(new_grid[0]), neighbors)
    for neighbor in neighbors:
        if not new_grid[neighbor[0]][neighbor[1]]:
            new_grid[neighbor[0]][neighbor[1]] = 1
            queue |= {neighbor}

print("\n".join(["".join(["#" if letter else " "for letter in line]) for line in new_grid]))



total = 0
for row in range(len(data)):
    for col in range(len(data[0])):
        good = True
        for r in range(row * 3, row * 3+ 3):
            for c in range(col * 3, col * 3 + 3):
                if new_grid[r][c]:
                    good = False
                    break
        if good:
            total += 1

print(total)