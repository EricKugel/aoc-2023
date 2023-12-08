from aoc_meta import *
aoc_init(2023, 4)

# data = [line[10:] for line in get_test_input().split("\n")]
data = [line[10:] for line in get_input().split("\n")]

cards = [1 for _ in range(199)]

for i, line in enumerate(data):
    winning, numbers = line.split("|")
    winning = list(map(int, map("".join, zip(*[iter(list(winning))]*3))))
    numbers = list(map(int, map("".join, zip(*[iter(list(numbers))]*3))))
    if (winners := sum([win in numbers for win in winning])) > 0:
       for j in range(winners):
           index = i + j + 1
           cards[index] += cards[i]

p2(sum(cards))