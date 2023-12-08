from aoc_meta import *
aoc_init(2023, 2)

data = [thing[8:] for thing in get_input().split("\n")]
games = []
for line in data:
    game = []
    for set in line.split("; "):
        set_dict = {}
        for num, color in map(str.split, set.split(", ")):
            set_dict[color] = int(num)
        game.append(set_dict)
    games.append(game)

too_high = {
    "red": 12,
    "green": 13, 
    "blue": 14
}

total = 0
for id, game in enumerate(games):
    product = 1
    for color in too_high.keys():
        colors = []
        for set in game:
            if color in set.keys():
                colors.append(set[color])
        product *= max(colors)

    total += product

p2(total)
# print(total)
