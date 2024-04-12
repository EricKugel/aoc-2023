from aoc_meta import *
aoc_init(2023, 24)

import itertools as it
import numpy as np 
from tqdm import tqdm

data = [tuple(map(int, line.replace(" @", ",").split(", "))) for line in get_input().split("\n")]
# data = [tuple(map(int, line.replace(" @", ",").split(", "))) for line in get_test_input().split("\n")]

def get_cross(stone1, stone2):
    x1, y1, z1, vx1, vy1, vz1 = stone1
    x2, y2, z2, vx2, vy2, vz2 = stone2
    vx1 -= vx
    vx2 -= vx
    vy1 -= vy
    vy2 -= vy

    velocities = np.array([[vx1, -vx2], [vy1, -vy2]])
    positions = np.array([x2 - x1, y2 - y1])

    try:
        t1, t2 = np.linalg.solve(velocities, positions)
    except:
        return False
    if t1 < 0 or t2 < 0: return False

    x, y = x1 + vx1 * t1, y1 + vy1 * t1
    
    return tuple(map(int, (x, y)))

def get_cross_for_z(stone1, stone2):
    x1, y1, z1, vx1, vy1, vz1 = stone1
    x2, y2, z2, vx2, vy2, vz2 = stone2
    vx1 -= vx
    vx2 -= vx
    vy1 -= vy
    vy2 -= vy
    vz1 -= vz
    vz2 -= vz

    velocities = np.array([[vx1, -vx2], [vy1, -vy2]])
    positions = np.array([x2 - x1, y2 - y1])

    try:
        t1, t2 = np.linalg.solve(velocities, positions)
    except:
        return False
    if t1 < 0 or t2 < 0: return False

    x, y, z = x1 + vx1 * t1, y1 + vy1 * t1, z1 + vz1 * t1
    
    return tuple(map(int, (x, y, z)))

max_velocity = 300

# for vx in tqdm(range(-max_velocity, max_velocity + 1)):
#     for vy in range(-max_velocity, max_velocity + 1):
#         current_cross = None
#         for comb in it.combinations(data[:3], 2):
#             cross = get_cross(*comb)
#             if not cross: break
#             if not current_cross:
#                 current_cross = get_cross(*comb)
#             else:
#                 if cross != current_cross:
#                     break
#         else:
#             print(f"{current_cross} at {(vx, vy)}")

# Now that I know the correct x and y velocity (242, 83) I can iterate over the z values
vx = 242
vy = 83
# vx = -3
# vy = 1
for vz in range(-max_velocity, max_velocity + 1):
    current_cross = None
    for comb in it.combinations(data[:3], 2):
        cross = get_cross_for_z(*comb)
        if not cross: continue
        if not current_cross:
            current_cross = cross
        else:
            if cross != current_cross:
                break
    else:
        print(sum(current_cross))