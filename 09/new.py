from aoc_meta import *
aoc_init(2023, 9)

import numpy as np 

data = [[int(num) for num in line.split(" ")]  for line in get_input().split("\n")]
# data = [[int(num) for num in line.split(" ")] for line in get_test_input().split("\n")]

total = 0
for line in data:
    levels = [line]
    while not all([num == 0 for num in levels[-1]]):
        levels.append([levels[-1][i + 1] - levels[-1][i] for i in range(len(levels[-1]) - 1)])
    for i in range(len(levels) - 1, 0, -1):
        levels[i - 1] = [levels[i - 1][0] - levels[i][0]] + levels[i - 1]
    total += levels[0][0]
p2(total)