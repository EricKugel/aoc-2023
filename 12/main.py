from aoc_meta import *
aoc_init(2023, 12)

import itertools as it
import functools as ft

from tqdm import tqdm

data = [(((springs + "?") * 5)[:-1], tuple(list(map(int, config.split(",")))) * 5) for springs, config in  map(str.split, get_input().split("\n"))]
# data = [(((springs + "?") * 5)[:-1], tuple(list(map(int, config.split(",")))) * 5) for springs, config in  map(str.split, get_test_input().split("\n"))]
# data = [(springs, tuple(map(int, config.split(",")))) for springs, config in  map(str.split, get_test_input().split("\n"))]

@ft.cache
def num_options(springs, config, size = 0):
    if len(config) == 0:
        return int("#" not in springs)
    if len(springs) == 0:
        return len(config) == 1 and size == config[0]
    if size > config[0]:
        return 0
    if springs[0] == "#":
        return num_options(springs[1:], config, size + 1)
    if springs[0] == ".":
        if size > 0:
            if size != config[0]:
                return 0
            return num_options(springs[1:], config[1:])
        return num_options(springs[1:], config)
    total = 0
    if springs[0] == "?":
        for is_hashtag in [True, False]:
            total += num_options(("#" if is_hashtag else ".") + (springs[1:] if len(springs) > 1 else ""), config, size)
    return total

p2(sum([num_options(*line) for line in tqdm(data)]))