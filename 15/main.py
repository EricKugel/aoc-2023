from aoc_meta import *
aoc_init(2023, 15)

from collections import OrderedDict

box = []
for _ in range(256):
    box.append(OrderedDict())

data = get_input().replace("\n", "")

def hash(thing):
    current = 0
    for char in thing:
        current += ord(char)
        current *= 17
        current %= 256
    return current

for thing in data.split(","):
    is_equal = "=" in thing
    label = thing[0:thing.index("=") if is_equal else thing.index("-")]
    if is_equal:
        focal_length = thing[thing.index("=") + 1:]
        box[hash(label)][label] = int(focal_length)
    else:
        if label in box[hash(label)].keys():
            del box[hash(label)][label]

total = 0
for i, actual_box in enumerate(box):
    for j, lens in enumerate(actual_box.items()):
        label, focal_length = lens
        total += (i + 1) * (j + 1) * focal_length

p2(total)