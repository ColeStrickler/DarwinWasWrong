import random
import sys

import numpy as np
from matplotlib import pyplot as plt

NUM_QUEENS = 27
NUM_POP = 10000

def init_population(num_pop):
    ret = []
    for i in range(num_pop):
        possible = [str(x) for x in range(0, NUM_QUEENS)]
        random.shuffle(possible)
        curr = []
        while len(possible):
            curr.append(possible.pop(0))
        ret.append(curr)
    return ret



def calcFitness(dna_string):
    board = [[f"{0}" for i in range(0,NUM_QUEENS)] for i in range(0,NUM_QUEENS)]
    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
    c = 0
    placements = []
    for r in dna_string:
        try:
            board[int(r)][c] = "Q"
        except Exception:
            print("\n\nEXIT")
            print(len(board))
            print(len(board[0]))
            print(placements)
            print(dna_string)
            print(r, c)
            sys.exit()
        placements.append((int(r),c))
        c += 1
    score = 0
    for p in placements:
        for d in directions:
            y, x = p
            y2, x2 = d
            new_y = y + y2
            new_x = x + x2
            while True:
                if new_x < 0 or new_x >= NUM_QUEENS or new_y < 0 or new_y >= NUM_QUEENS:
                    break
                if board[new_y][new_x] == "Q":
                    score += 1
                y2, x2 = d
                new_y += y2
                new_x += x2
    return score

def rankFitness(population):
    population.sort(key=lambda x: calcFitness(x))

def mutate(dna_string, mutation_rate=0.04):
    chars = dna_string
    if random.random() < mutation_rate:
        p1 = random.randint(1, len(dna_string) - 2)
        p2 = random.randint(1, len(dna_string) - 2)
        tmp = chars[p1]
        chars[p1] = chars[p2]
        chars[p2] = tmp
    return chars




def selection(population):
    new_gen = []
    rankFitness(population)
    elite = population[0:int(len(population) / 5)]
    new_gen += elite
    num = len(new_gen)

    successful = population[0:int(len(population) / 3)]
    while num < NUM_POP:
        m1 = successful[(random.randrange(len(successful)))]
        m2 = successful[(random.randrange(len(successful)))]
        new_gen += repr(m1, m2)
        num += 2

    for i in range(len(elite), len(new_gen)):
        new_gen[i] = mutate(new_gen[i])
    return new_gen




def repr(m1, m2):
    c1_num = int(len(m1)/2)
    c1 = random.randint(0, c1_num)
    c2 = random.randint(c1_num, len(m1) - 1)

    possible1 = [str(x) for x in range(0, NUM_QUEENS)]
    possible2 = [str(x) for x in range(0, NUM_QUEENS)]

    dna_1 = m1[c1:c2]
    dna_2 = m2[c1:c2]
    for i in range(len(dna_1)):
        if dna_1[i] in possible1:
            possible1.remove(dna_1[i])
        if dna_2[i] in possible2:
            possible2.remove(dna_2[i])

    i = 0

    while i < c1:
        dna_1.append(possible1[0])
        dna_2.append(possible2[0])
        possible1.pop(0)
        possible2.pop(0)
        i += 1

    while len(possible1):
        dna_1.append(possible1[0])
        dna_2.append(possible2[0])
        possible1.pop(0)
        possible2.pop(0)


    return [dna_2, dna_1]


pop = init_population(NUM_POP)
rankFitness(pop)
best = calcFitness(pop[0])
worst = 999
max_vals = []
gen = 0
while best != 0:
    max_vals.append(best)
    print(f"Generations: {gen}, Best: {best}")
    pop = selection(pop)
    best = calcFitness(pop[0])
    gen += 1

board = [[f"{0}" for i in range(0,NUM_QUEENS)] for i in range(0,NUM_QUEENS)]
c = 0
for r in pop[0]:
    board[int(r)][c] = "Q"
    c += 1

print(np.matrix(board))

plt.plot(max_vals, color='red')
#plt.plot(mean_vals, color='green')
plt.xlabel('Generation')
plt.ylabel('Max/Mean')

plt.title('Max and Average fitness over Generations')
plt.show()