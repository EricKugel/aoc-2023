from aoc_meta import *
aoc_init(2023, 5)

data = get_input().split("\n\n")

# all seeds are ranges
seeds = []
for start, length in zip(*[iter(list(map(int, data[0].split(" ")[1:])))]*2):
    seeds.append((start, start + length))

for maps in data:
    new_seeds = []
    used_seeds = []
    for line in maps.split("\n")[1:]:
        dest, src, length = map(int, line.split(" "))
        for seed_start, seed_end in seeds:
            if ((src < seed_start and src + length > seed_start) or (src + length >= seed_end and src < seed_end) or (src >= seed_start and src + length < seed_end)) and not (seed_start, seed_end) in used_seeds:
                unused = [(seed_start, src)] if src > seed_start else []
                used = (max(src, seed_start), min(seed_end, src + length))
                if seed_end > src + length:
                    unused.append((src + length, seed_end))
                used_seeds.append((seed_start, seed_end))
                new_seeds.append((max(src, seed_start) + (dest - src), min(seed_end, src + length) + (dest - src)))
                seeds += unused
    seeds = new_seeds + list(filter(lambda seed : seed not in used_seeds, seeds))

p2(min(seeds)[0])