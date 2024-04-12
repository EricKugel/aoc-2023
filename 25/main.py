from aoc_meta import *
aoc_init(2023, 25)

import networkx as nx
import math

data = "\n".join([line.replace(":", "") for line in get_input().split("\n")])
with open("output.txt", "w") as file:
    file.write(data)

g = nx.read_adjlist("output.txt")
for node1, node2 in nx.minimum_edge_cut(g):
    g.remove_edge(node1, node2)
p1(math.prod(map(len, nx.connected_components(g))))