from aoc_meta import *
aoc_init(2023, 24)

import itertools as it
import numpy as np
from scipy.optimize import fsolve

# data = [tuple(map(int, line.replace(" @", ",").split(", "))) for line in get_input().split("\n")[:3]]
data = [tuple(map(int, line.replace(" @", ",").split(", "))) for line in get_test_input().split("\n")[:3]]
x1, y1, z1, vx1, vy1, vz1 = data[0]
x2, y2, z2, vx2, vy2, vz2 = data[1]
x3, y3, z3, vx3, vy3, vz3 = data[2]

vx, vy, vz = [-3, 1, 2]

def f(X):
    F = np.zeros(10)
    F[0] = X[3] - (vx1 - vx) * X[0] - x1
    F[1] = X[4] - (vy1 - vx) * X[0] - y1
    F[2] = X[5] - (vz1 - vx) * X[0] - z1
    F[3] = X[3] - (vx2 - vy) * X[1] - x2
    F[4] = X[4] - (vy2 - vy) * X[1] - y2
    F[5] = X[5] - (vz2 - vy) * X[1] - z2
    F[6] = X[3] - (vx3 - vz) * X[2] - x3
    F[7] = X[4] - (vy3 - vz) * X[2] - y3
    F[8] = X[5] - (vz3 - vz) * X[2] - z3
    F[9] = max([abs(X[i] - int(X[i])) for i in range(10)[3:9]])
    return F

solution = fsolve(f, np.array([0, 0, 0, 0, 0, 0, -3, 1, 2, 0]), full_output = 1)[0].tolist()
print(sum(solution))