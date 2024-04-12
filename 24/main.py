from aoc_meta import *
aoc_init(2023, 24)

import itertools as it
import numpy as np 
from tqdm import tqdm

data = [tuple(map(int, line.replace(" @", ",").split(", "))) for line in get_input().split("\n")]
# data = [tuple(map(int, line.replace(" @", ",").split(", "))) for line in get_test_input().split("\n")]

bounds = (200000000000000, 400000000000000)

def do_they_cross(stone1, stone2):
    x1, y1, z1, vx1, vy1, vz1 = stone1
    x2, y2, z2, vx2, vy2, vz2 = stone2
    velocities = np.array([[vx1, -vx2], [vy1, -vy2]])
    positions = np.array([x2 - x1, y2 - y1])

    try:
        t1, t2 = np.linalg.solve(velocities, positions)
    except:
        return False
    if t1 < 0 or t2 < 0: return False

    x, y = x1 + vx1 * t1, y1 + vy1 * t1
    return bounds[0] <= x <= bounds[1] and bounds[0] <= y <= bounds[1]

p1(sum(it.starmap(do_they_cross, tqdm(it.combinations(data, 2)))))