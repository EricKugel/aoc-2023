from aoc_meta import *
aoc_init(2023, 13)

# data = list(zip(*[[tuple(map(tuple, pattern.split("\n"))) for pattern in get_input().split("\n\n")]]*2))
# data = list(zip(*[[tuple(map(tuple, pattern.split("\n"))) for pattern in get_test_input().split("\n\n")]]*2))
data = ([pattern.split("\n") for pattern in get_input().split("\n\n")])
# data = ([pattern.split("\n") for pattern in get_test_input().split("\n\n")])

from tqdm import tqdm

def get_count(cluster, old_count):
    pattern0 = cluster
    pattern1 = list(map("".join, zip(*pattern0[::-1])))
    pattern2 = list(map("".join, zip(*pattern1[::-1])))
    pattern3 = list(map("".join, zip(*pattern2[::-1])))
    patterns = [pattern0, pattern1, pattern2, pattern3]
    
    try:
        i = 0
        while True:
            for rotation, pattern in enumerate(patterns):
                if i < len(pattern) - 1 and pattern[i] == pattern[-1]:
                    offset = i
                    reflected_pattern = pattern[offset:]
                    if len(reflected_pattern) % 2 != 0:
                        continue
                    for j, line in enumerate(reflected_pattern[:-1]):
                        if line != reflected_pattern[-(j + 1)]:
                            break
                    else:
                        count = i + len(reflected_pattern) // 2
                        if rotation in [2, 3]:
                            count = len(pattern) - count
                        if rotation in [0, 2]:
                            count *= 100
                        if count == old_count:
                            continue
                        break
            else:
                i += 1
                if all([i > len(pattern) for pattern in patterns]):
                    return 0
                continue
            return count
    except:
        return 0

total = []
for cluster in data:
    old_count = get_count(cluster, 0)
    new_count = 0
    for i, line in enumerate(cluster):
        if new_count != 0 and new_count != old_count:
            break
        for j, char in enumerate(line):
            new_cluster = cluster[0:i] + [line[0:j] + ("#" if char == "." else ".") + line[j + 1:]] + cluster[i + 1:]
            if (new_count := get_count(new_cluster, old_count)) != old_count and new_count != 0:
                total.append(new_count)
                # print(new_count, "\n\n")
                break

p2(sum(total))