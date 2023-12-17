
def check(springs, config):
    tuple(map(len, (filter(lambda spring : len(spring) > 0, new_springs.split(".")))))

total = 0
for springs, config in tqdm(data):
    unknowns = springs.count("?") 
    
    combs = []
    for x in range(2 ** unknowns):
        string = format(x, "b").zfill(unknowns)
        combs.append(["#" if letter == "1" else "." for letter in string])
    
    for comb in combs:
        i = 0
        new_comb = ""
        for letter in springs:
            if letter in "#.":
                new_comb += letter
            else:
                new_comb += comb[i]
                i += 1
        comb = new_comb
    
        new_springs = tuple(map(len, (filter(lambda spring : len(spring) > 0, new_springs.split(".")))))
        sub_total += new_springs == config

    total += sub_total
p1(total)