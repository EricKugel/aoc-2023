from aoc_meta import *
aoc_init(2023, 23)

# data = get_test_input()
data = get_input()
for slope in ">v<^":
    data = data.replace(slope, ".")
data = data.split("\n")
# data = get_test_input().split("\n")
shape = (len(data), len(data[0]))
directions = [1j, 1, -1j, -1]

grid = {}
for i, line in enumerate(data):
    for j, letter in enumerate(line):
        grid[(i + j * 1j)] = letter

goal = complex(shape[0] - 1, shape[1] - 2)

# No shot this steaming spaghetti actually works 😭
edges = {}
queue = [(1j)]
while queue:
    coords = queue.pop()
    if coords in edges: continue
    edges[coords] = []
    valid_d = []
    for d in directions:
        new_coords = coords + d
        if new_coords not in grid: continue
        if grid[new_coords] == ".": valid_d.append(d)
    for d in valid_d:
        new_coords = coords + d
        path = [coords]
        while grid[new_coords] == ".":
            path.append(new_coords)
            valid_dd = []
            for dd in directions:
                new_new_coords = new_coords + dd
                if new_new_coords not in grid: continue
                if new_new_coords in path: continue
                if grid[new_new_coords] == ".": valid_dd.append(dd)
            if len(valid_dd) != 1: break
            new_coords = new_coords + valid_dd[0]
        edges[coords].append((path[-1], len(path) - 1))
        queue.append(path[-1])

paths = [[(1j, 0)]]
lengths = []
while paths:
    path = paths[-1]
    coords, size = path[-1]
    if coords == goal:
        lengths.append(size)
        paths.pop()
        continue
    paths.pop()
    for new_coords, steps in edges[coords]:
        if new_coords in map(lambda node : node[0], path): continue
        paths.append(path + [(new_coords, size + steps)])

print(max(lengths))