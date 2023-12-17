from aoc_meta import *
aoc_init(2023, 16)

data = get_input().split("\n")

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

energized = set()
straight_pipes = set()

def trace(coord, dir):
    global energized, straight_pipes
    for _ in range(10000):
        dir %= 4
        new_coord = (coord[0] + directions[dir][0], coord[1] + directions[dir][1])
        if not (0 <= new_coord[0] < len(data) and 0 <= new_coord[1] < len(data[0])):
            return
        energized |= {new_coord}
        tile = data[new_coord[0]][new_coord[1]]
        if tile != ".":
            if tile == "\\":
                dir += 1 if dir in [0, 2] else -1
            elif tile == "/":
                dir += 1 if dir in [1, 3] else -1
            elif tile == "-":
                if dir in [0, 2]: 
                    coord = new_coord
                    continue
                if new_coord not in straight_pipes:
                    straight_pipes |= {new_coord}
                    trace(new_coord, dir + 1)
                    dir -= 1
                else:
                    return
            elif tile == "|":
                if dir in [1, 3]:
                    coord = new_coord
                    continue
                if new_coord not in straight_pipes:
                    straight_pipes |= {new_coord}
                    trace(new_coord, dir + 1)
                    dir -= 1
                else:
                    return
        coord = new_coord

all_starts = []
for row in range(len(data)):
    all_starts.append(((row, -1), 0))
    all_starts.append(((row, len(data[0])), 2))
for col in range(len(data[0])):
    all_starts.append(((-1, col), 1))
    all_starts.append(((len(data), col), 3))
for i in range(len(all_starts)):
    energized = set()
    straight_pipes = set()
    trace(*all_starts[i])
    all_starts[i] = len(energized)

p2(max(all_starts))