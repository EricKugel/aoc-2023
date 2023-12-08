from aoc_meta import *
aoc_init(2023, 6)

import tqdm

data = []
for line in get_input().split("\n"):
    num = ""
    for letter in line:
        if letter in "1234567890":
            num += letter
    data.append(int(num))
time, distance = data

def check(acceleration_time):
    return (time - acceleration_time) * acceleration_time > distance

p2(sum([check(acceleration_time) for acceleration_time in tqdm.tqdm(range(time))]))