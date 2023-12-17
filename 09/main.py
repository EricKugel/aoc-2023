from aoc_meta import *
aoc_init(2023, 9)

import numpy as np 

data = [[int(num) for num in line.split(" ")]  for line in get_input().split("\n")]

def fit(nums, degree):
    x = list(range(len(nums)))
    coefficients = np.polyfit(x, nums, degree)
    curve = np.poly1d(coefficients)
    predicted = curve(x)
    actual = np.sum(nums) / len(nums)
    ssreg = np.sum((predicted - actual) ** 2)
    sstot = np.sum((nums - actual) ** 2)
    return curve, ssreg / sstot

total = 0
for line in data:
    deg = 0
    while (results :=  fit(line, deg))[1] < .9999999:
        deg += 1
    total += int(results[0](len(line)))

print(total)