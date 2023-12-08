from aoc_meta import *
aoc_init(2023, 1)

data = get_input().split("\n")

letters = [None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0 
for line in data:
    first = -1
    last = -1

    front_line = ""
    back_line = ""
    for letter in line:
        if first == -1:
            if letter in "1234567890":
                first = int(letter)
            front_line += letter
            for i, thing in enumerate(letters):
                if thing:
                    front_line = front_line.replace(thing, str(i))
                    for new_letter in front_line:
                        if new_letter in "1234567890":
                            first = int(new_letter)
        else:
            break
    for letter in line[::-1]:
        if last == -1:
            if letter in "1234567890":
                last = int(letter)
            back_line += letter
            for i, thing in enumerate(letters):
                if thing:
                    back_line = back_line.replace(thing[::-1], str(i))
                    for new_letter in back_line:
                        if new_letter in "1234567890":
                            last = int(new_letter)
        else:
            break
    total += first * 10 + last
    print(first * 10 + last)

p2(total)