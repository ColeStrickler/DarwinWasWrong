import json
import random
"""
graph = {"A": {"B": 12, "C": 29, "D": 22, "E": 13, "F": 24},
         "B": {"A": 12, "C": 19, "D": 3, "E": 25, "F": 6},
         "C": {"A": 29, "B": 19, "D": 21, "E": 23, "F": 28},
         "D": {"A": 22, "B": 3, "C": 21, "E": 4, "F": 5},
         "E": {"A": 13, "B": 25, "C": 23, "D": 4, "F": 16},
         "F": {"A": 24, "B": 6, "C": 28, "D": 5, "E": 16}}
         
         
         https://developers.google.com/optimization/routing/tsp
         graph = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ]

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
ret_dict = {}
x = 0
for l in letters:
    ret_dict[l] = {}
    for i in range(len(graph[x])):
        ret_dict[l][letters[i]] = graph[x][i]
    x += 1

         
"""




#print(json.dumps(ret_dict))

graph = {'A': {'A': 0, 'B': 2451, 'C': 713, 'D': 1018, 'E': 1631, 'F': 1374, 'G': 2408, 'H': 213, 'I': 2571, 'J': 875, 'K': 1420, 'L': 2145, 'M': 1972}, 'B': {'A': 2451, 'B': 0, 'C': 1745, 'D': 1524, 'E': 831, 'F': 1240, 'G': 959, 'H': 2596, 'I': 403, 'J': 1589, 'K': 1374, 'L': 357, 'M': 579}, 'C': {'A': 713, 'B': 1745, 'C': 0, 'D': 355, 'E': 920, 'F': 803, 'G': 1737, 'H': 851, 'I': 1858, 'J': 262, 'K': 940, 'L': 1453, 'M': 1260}, 'D': {'A': 1018, 'B': 1524, 'C': 355, 'D': 0, 'E': 700, 'F': 862, 'G': 1395, 'H': 1123, 'I': 1584, 'J': 466, 'K': 1056, 'L': 1280, 'M': 987}, 'E': {'A': 1631, 'B': 831, 'C': 920, 'D': 700, 'E': 0, 'F': 663, 'G': 1021, 'H': 1769, 'I': 949, 'J': 796, 'K': 879, 'L': 586, 'M': 371}, 'F': {'A': 1374, 'B': 1240, 'C': 803, 'D': 862, 'E': 663, 'F': 0, 'G': 1681, 'H': 1551, 'I': 1765, 'J': 547, 'K': 225, 'L': 887, 'M': 999}, 'G': {'A': 2408, 'B': 959, 'C': 1737, 'D': 1395, 'E': 1021, 'F': 1681, 'G': 0, 'H': 2493, 'I': 678, 'J': 1724, 'K': 1891, 'L': 1114, 'M': 701}, 'H': {'A': 213, 'B': 2596, 'C': 851, 'D': 1123, 'E': 1769, 'F': 1551, 'G': 2493, 'H': 0, 'I': 2699, 'J': 1038, 'K': 1605, 'L': 2300, 'M': 2099}, 'I': {'A': 2571, 'B': 403, 'C': 1858, 'D': 1584, 'E': 949, 'F': 1765, 'G': 678, 'H': 2699, 'I': 0, 'J': 1744, 'K': 1645, 'L': 653, 'M': 600}, 'J': {'A': 875, 'B': 1589, 'C': 262, 'D': 466, 'E': 796, 'F': 547, 'G': 1724, 'H': 1038, 'I': 1744, 'J': 0, 'K': 679, 'L': 1272, 'M': 1162}, 'K': {'A': 1420, 'B': 1374, 'C': 940, 'D': 1056, 'E': 879, 'F': 225, 'G': 1891, 'H': 1605, 'I': 1645, 'J': 679, 'K': 0, 'L': 1017, 'M': 1200}, 'L': {'A': 2145, 'B': 357, 'C': 1453, 'D': 1280, 'E': 586, 'F': 887, 'G': 1114, 'H': 2300, 'I': 653, 'J': 1272, 'K': 1017, 'L': 0, 'M': 504}, 'M': {'A': 1972, 'B': 579, 'C': 1260, 'D': 987, 'E': 371, 'F': 999, 'G': 701, 'H': 2099, 'I': 600, 'J': 1162, 'K': 1200, 'L': 504, 'M': 0}}






NUM_POP = 10000



def init_population(population_num, dna_len):
    ret = []
    for i in range(population_num):
        curr = ""
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
        for j in range(len(letters)):
            sel = random.randint(0,len(letters) - 1)
            letter = letters[sel]
            letters.pop(sel)
            curr += str(letter)
        curr += curr[0]
        ret.append(curr)
    return ret

def calcFitness(dna_string):
    fitness = 0
    for i in range(len(dna_string) - 1):
        src = dna_string[i]
        dst = dna_string[i + 1]
        fitness += graph[src][dst]
    return fitness

def rankFitness(population):
    population.sort(key=lambda x: calcFitness(x))


def repr(m1, m2):
    c1_num = int(len(m1)/2)
    c1 = random.randint(0, c1_num)
    c2 = random.randint(c1_num, len(m1) - 1)

    possible1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    possible2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

    dna_1 = m1[c1:c2]
    dna_2 = m2[c1:c2]
    for i in range(len(dna_1)):
        if dna_1[i] in possible1:
            possible1.remove(dna_1[i])
        if dna_2[i] in possible2:
            possible2.remove(dna_2[i])

    i = 0

    while i < c1:
        dna_1 = str(possible1[0]) + dna_1
        dna_2 = str(possible2[0]) + dna_2
        possible1.pop(0)
        possible2.pop(0)
        i += 1

    while len(possible1):
        dna_1 += str(possible1[0])
        dna_2 += str(possible2[0])
        possible1.pop(0)
        possible2.pop(0)

    dna_1 += dna_1[0]
    dna_2 += dna_2[0]

    return [dna_2, dna_1]


def mutate(dna_string, mutation_rate=0.12):
    chars = list(dna_string)
    if random.random() < mutation_rate:
        p1 = random.randint(1, len(dna_string) - 2)
        p2 = random.randint(1, len(dna_string) - 2)
        tmp = chars[p1]
        chars[p1] = chars[p2]
        chars[p2] = tmp
    return ''.join(chars)

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



pop = init_population(NUM_POP, 0)
rankFitness(pop)
gen = 0
best = calcFitness(pop[0])
best_str = pop[0]

print(f"GENERATION: {gen}, BEST: {best} --> {best_str}")
while gen < 1000 and best != 7293:
    best = calcFitness(pop[0])
    best_str = pop[0]
    print(f"GENERATION: {gen}, BEST: {best} --> {best_str}")
    pop = selection(pop)
    gen += 1
print(f"GENERATION: {gen}, BEST: {best} --> {best_str}")