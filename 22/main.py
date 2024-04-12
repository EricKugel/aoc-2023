from aoc_meta import *
aoc_init(2023, 22)

from tqdm import tqdm

bricks = []
currently_tested = None
class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.cubes = []
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    self.cubes.append((x, y, z))
        self.supported_by = None
        bricks.append(self)
    def is_supported(self):
        lowest_z = self.get_lowest_z()
        if not self.supported_by:
            self.supported_by = set()
            [brick.supports(self) for brick in bricks]
        if lowest_z == 1: return True
        return len(self.supported_by) > 0
    def supports(self, brick):
        if brick == self: return False
        lowest_z = brick.get_lowest_z()
        for cube in filter(lambda cube : cube[2] == lowest_z, brick.cubes):
            if (cube[0], cube[1], cube[2] - 1) in self.cubes:
                brick.supported_by.add(self)
                return
        return
    def fall(self):
        if not self.is_supported():
            new_cubes = []
            for cube in self.cubes:
                new_cubes.append((cube[0], cube[1], cube[2] - 1))
            self.cubes = new_cubes
    def __repr__(self):
        lowest_x = min(self.cubes, key = lambda cube : cube[0])[0]
        highest_x = max(self.cubes, key = lambda cube : cube[0])[0]
        lowest_y = min(self.cubes, key = lambda cube : cube[1])[1]
        highest_y = max(self.cubes, key = lambda cube : cube[1])[1]
        lowest_z = min(self.cubes, key = lambda cube : cube[2])[2]
        highest_z = max(self.cubes, key = lambda cube : cube[2])[2]
        return f"{"?"}: {lowest_x},{lowest_y},{lowest_z}~{highest_x},{highest_y},{highest_z}"
    def get_lowest_z(self):
        return min(self.cubes, key = lambda cube : cube[2])[2]

def unstable():
    return any([not brick.is_supported() for brick in bricks])

def stable_without(brick):
    global currently_tested
    currently_tested = brick
    return not unstable()

def visualize(show_axis):
    grid = {}
    for brick in bricks:
        l_x, l_y, l_z, h_x, h_y, h_z = map(int, str(brick)[3:].replace("~", ",").split(","))
        for z in range(l_z, h_z + 1):
            for col in (range(l_x, h_x + 1) if show_axis == "x" else range(l_y, h_y + 1)):
                if (z, col) in grid:
                    grid[(z, col)] = "?"
                else:
                    grid[(z, col)] = brick.letter
    l_z = min(grid.keys(), key = lambda coords : coords[0])[0]
    h_z = max(grid.keys(), key = lambda coords : coords[0])[0]
    l_col = min(grid.keys(), key = lambda coords : coords[1])[1]
    h_col = max(grid.keys(), key = lambda coords : coords[1])[1]
    output = ""
    for z in range(l_z, h_z + 1)[::-1]:
        for col in range(l_col, h_col + 1):
            if not (z, col) in grid:
                output += "."
            else:
                output += grid[(z, col)]
        output += "\n"
    print(output, "\n\n")

def get_supported(brick):
    queue = [brick]
    supported = []
    while queue:
        brick = queue.pop()
        for other in bricks:
            if len(other.supported_by) > 0 and all([others_support in supported or others_support == brick for others_support in other.supported_by]):
                if other not in supported:
                    supported.append(other)
                    queue.append(other)
    return len(supported)

data = [list(map(int, line.replace("~", ",").split(","))) for line in get_input().split("\n")]
# data = [list(map(int, line.replace("~", ",").split(","))) for line in get_test_input().split("\n")]

for i, line in enumerate(data): Brick(*line)
bricks.sort(key = lambda brick : brick.get_lowest_z())
for brick in bricks:
    while not brick.is_supported():
        brick.fall()

# visualize("x")
# visualize("y")

print(sum(map(get_supported, tqdm(bricks))))