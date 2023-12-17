from aoc_meta import *
aoc_init(2023, 14)

import functools

data = tuple(map(tuple, get_input().split("\n")))

configs = []

def roll(config):
    config = list(map(list, config))
    for i, line in enumerate(config):
        for j, char in enumerate(line):
            if char == "O":
                new_i = i - 1
                while new_i > -1 and (space := config[new_i][j]) != "#" and space != "O":
                    new_i -= 1
                new_i += 1
                config[i][j] = "."
                config[new_i][j] = "O"
    return config

def cycle(config):
    for i in range(4):
        config = roll(config)
        config = tuple(map(tuple, zip(*config[::-1])))
    return config

for i in range(1000000000):
    data = cycle(data)
    if data in configs:
        repeat_index = configs.index(data)
        break
    configs.append(data)

repeats = configs[repeat_index:]
data = repeats[(1000000000 - repeat_index - 1) % len(repeats)]
print(sum([(len(data) - j) * line.count("O") for j, line in enumerate(data)]))
