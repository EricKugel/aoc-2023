from aoc_meta import *
aoc_init(2023, 8)

import re
import math

data = get_input().split("\n")
instructions = data[0]
nodes = dict([((result := re.search(r"(.+) = \((.+), (.+)\)", line).groups())[0], (result[1], result[2])) for line in data[2:]])

current_nodes = [node for node in nodes.keys() if node.endswith("A")]
for i, node in enumerate(current_nodes):
    steps = 0
    while not node.endswith("Z"):
        instruction = instructions[steps % len(instructions)]
        node = nodes[node][0 if instruction == "L" else 1]
        steps += 1
    current_nodes[i] = steps

p2(math.lcm(*current_nodes))