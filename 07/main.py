from aoc_meta import *
aoc_init(2023, 7)

from functools import cmp_to_key

data = list(map(str.split, get_input().split("\n")))

ranks = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def get_score(hand):
    num_wild = hand.count("J")
    hand = "".join([letter for letter in list(hand) if letter != "J"])
    if len(hand) == 0:
        return 7

    cards = dict([(letter, hand.count(letter)) for letter in set(hand)])
    cards[max(set(hand), key = hand.count)] += num_wild
    values = cards.values()

    if max(values) == 5:
        return 7
    if max(values) == 4:
        return 6
    if 3 in values and 2 in values:
        return 5
    if 3 in values:
        return 4
    if list(values).count(2) > 1:
        return 3
    if 2 in values: 
        return 2
    return 1

def does_win(hand, other):
    hand, other = hand[0], other[0]
    score, other_score = get_score(hand), get_score(other)
    if score != other_score:
        return 1 if score > other_score else -1
    for i in range(len(hand)):
        card, other_card = hand[i], other[i]
        if card != other_card:
            return 1 if ranks.index(card) < ranks.index(other_card) else -1

data = sorted(data, key=cmp_to_key(does_win))
p2(sum([int(line[1]) * (i + 1) for i, line in enumerate(data)]))