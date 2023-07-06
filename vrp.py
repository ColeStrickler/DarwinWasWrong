import random
import sys

graph = {'A': {'A': 0, 'B': 2451, 'C': 713, 'D': 1018, 'E': 1631, 'F': 1374, 'G': 2408, 'H': 213, 'I': 2571, 'J': 875, 'K': 1420, 'L': 2145, 'M': 1972}, 'B': {'A': 2451, 'B': 0, 'C': 1745, 'D': 1524, 'E': 831, 'F': 1240, 'G': 959, 'H': 2596, 'I': 403, 'J': 1589, 'K': 1374, 'L': 357, 'M': 579}, 'C': {'A': 713, 'B': 1745, 'C': 0, 'D': 355, 'E': 920, 'F': 803, 'G': 1737, 'H': 851, 'I': 1858, 'J': 262, 'K': 940, 'L': 1453, 'M': 1260}, 'D': {'A': 1018, 'B': 1524, 'C': 355, 'D': 0, 'E': 700, 'F': 862, 'G': 1395, 'H': 1123, 'I': 1584, 'J': 466, 'K': 1056, 'L': 1280, 'M': 987}, 'E': {'A': 1631, 'B': 831, 'C': 920, 'D': 700, 'E': 0, 'F': 663, 'G': 1021, 'H': 1769, 'I': 949, 'J': 796, 'K': 879, 'L': 586, 'M': 371}, 'F': {'A': 1374, 'B': 1240, 'C': 803, 'D': 862, 'E': 663, 'F': 0, 'G': 1681, 'H': 1551, 'I': 1765, 'J': 547, 'K': 225, 'L': 887, 'M': 999}, 'G': {'A': 2408, 'B': 959, 'C': 1737, 'D': 1395, 'E': 1021, 'F': 1681, 'G': 0, 'H': 2493, 'I': 678, 'J': 1724, 'K': 1891, 'L': 1114, 'M': 701}, 'H': {'A': 213, 'B': 2596, 'C': 851, 'D': 1123, 'E': 1769, 'F': 1551, 'G': 2493, 'H': 0, 'I': 2699, 'J': 1038, 'K': 1605, 'L': 2300, 'M': 2099}, 'I': {'A': 2571, 'B': 403, 'C': 1858, 'D': 1584, 'E': 949, 'F': 1765, 'G': 678, 'H': 2699, 'I': 0, 'J': 1744, 'K': 1645, 'L': 653, 'M': 600}, 'J': {'A': 875, 'B': 1589, 'C': 262, 'D': 466, 'E': 796, 'F': 547, 'G': 1724, 'H': 1038, 'I': 1744, 'J': 0, 'K': 679, 'L': 1272, 'M': 1162}, 'K': {'A': 1420, 'B': 1374, 'C': 940, 'D': 1056, 'E': 879, 'F': 225, 'G': 1891, 'H': 1605, 'I': 1645, 'J': 679, 'K': 0, 'L': 1017, 'M': 1200}, 'L': {'A': 2145, 'B': 357, 'C': 1453, 'D': 1280, 'E': 586, 'F': 887, 'G': 1114, 'H': 2300, 'I': 653, 'J': 1272, 'K': 1017, 'L': 0, 'M': 504}, 'M': {'A': 1972, 'B': 579, 'C': 1260, 'D': 987, 'E': 371, 'F': 999, 'G': 701, 'H': 2099, 'I': 600, 'J': 1162, 'K': 1200, 'L': 504, 'M': 0}}

NUM_POP = 1000

def init_population(population_num):
    ret = []
    for i in range(population_num):
        curr = [[], [], []]
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
        starting_sel = random.randint(0, len(letters) - 1)
        starting_letter = letters[starting_sel]
        for e in curr:
            e.append(starting_letter)
        letters.pop(starting_sel)
        while len(letters):
            letter_sel = random.randint(0, len(letters) - 1)
            sel = random.randint(0, 2)
            curr[sel].append(letters[letter_sel])
            letters.pop(letter_sel)
        for e in curr:
            e.append(starting_letter)
        ret.append(curr)
    return ret

def calcFitness(individual):
    if len(individual) != 3:
        sys.exit()


    worst = -999
    for dna_string in individual:
        fitness = 0
        for i in range(len(dna_string) - 2):
            src = dna_string[i]
            dst = dna_string[i + 1]
            fitness += graph[src][dst]
        worst = max(worst, fitness)
    return worst

def rankFitness(population):
    population.sort(key=lambda x: calcFitness(x))

def mutate(individual, mutation_rate=0.22):
    for i in individual:
        if len(i) < 3:
            return individual

    if random.random() < mutation_rate:
        s1 = random.randint(0,2)
        s2 = random.randint(0,2)
        used_len = 0
        if len(individual[s1]) > len(individual[s2]):
            used_len = len(individual[s2])
        else:
            used_len = len(individual[s1])

        p1_1 = random.randint(1, int(used_len/2))
        p1_2 = random.randint(int(used_len/2), used_len - 2)

        tmp = individual[s1][p1_1:p1_2]
        two = individual[s2][p1_1:p1_2]
        if tmp not in individual[s2][p1_1:p1_2] and two not in individual[s1][p1_1:p1_2]:
            individual[s1][p1_1:p1_2] = two
            individual[s2][p1_1:p1_2] = tmp
    return individual


def repr(m1, m2):
    possible1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    possible2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

    dna_1 = [[], [], []]
    dna_2 = [[], [], []]
    c1_dict = {}
    y = 0
    for r in range(len(m1)):
        use_len = 0
        if len(m1[r]) > len(m2[r]):
            use_len = len(m2[r])
        else:
            use_len = len(m1[r])
        c1_num = int(use_len / 2)
        c1 = random.randint(0, c1_num)
        c2 = random.randint(c1_num, len(m1[r]) - 1)
        c1_dict[y] = c1
        dna_1[r] = m1[r][c1:c2]
        dna_2[r] = m2[r][c1:c2]

        for i in range(len(dna_1[r])):
            if len(dna_1[r]) < i and dna_1[r][i] in possible1:
                possible1.remove(dna_1[r][i])
            if len(dna_2[r]) > i:
                if dna_2[r][i] in possible2:
                    possible2.remove(dna_2[r][i])
        y += 1
    i = 0
    y = 0
    c1 = c1_dict[y]
    while i < c1:
        if len(possible1):
            dna_1[y] = [possible1[0]] + dna_1[y]
            possible1.pop(0)
        if len(possible2):
            dna_2[y] = [possible2[0]] + dna_2[y]
            possible2.pop(0)

        i += 1
        y += 1
        y %= 3
        c1 = c1_dict[y]
    while len(possible1):
        if len(possible1):
            dna_1[y] += [possible1[0]]
            possible1.pop(0)
        if len(possible2):
            dna_2[y] += [possible2[0]]
            possible2.pop(0)
        y += 1
        y %= 3
        c1 = c1_dict[y]


    for r in range(3):
        try:
            if len(dna_1[r]):
                dna_1[r] += [dna_1[r][0]]
            if len(dna_2[r]):
                dna_2[r] += [dna_2[r][0]]
        except Exception:
            print("Error adding r")
            print(dna_1, dna_2, r)
            sys.exit()

    return [dna_2, dna_1]

def selection(population):
    new_gen = []
    rankFitness(population)
    elite = population[0:int(len(population)/5)]
    new_gen += elite
    num = len(new_gen)

    successful = population[0:int(len(population)/3)]
    while num < NUM_POP:
        m1 = successful[(random.randrange(len(successful)))]
        m2 = successful[(random.randrange(len(successful)))]
        new_gen += repr(m1, m2)
        num += 2




    for i in range(len(elite), len(new_gen)):
        new_gen[i] = mutate(new_gen[i])


    return new_gen



pop = init_population(NUM_POP)
rankFitness(pop)
gen = 0
best = calcFitness(pop[0])
best_str = pop[0]

print(f"GENERATION: {gen}, BEST: {best} --> {best_str}")
while gen < 1000:
    best = calcFitness(pop[0])
    best_str = pop[0]
    print(f"GENERATION: {gen}, BEST: {best} --> {best_str}")
    pop = selection(pop)

    for p in pop:
        for i in p:
            if any(isinstance(el, list) for el in i):
                print(f"FOUND ERROR: {i},{p}")
    gen += 1
print(f"GENERATION: {gen}, BEST: {best} --> {best_str}")