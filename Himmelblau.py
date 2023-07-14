import math
import random

import numpy as np
from math import *

MIN = -5.0
MAX = 5.0

POPULATION_NUMBER = 200


gen = 0

found_minima = []
settled = []

def AlreadyFound(best, found_minima):
    best_x, best_y = best
    for x,y in found_minima:
        if (abs(x - best_x) <= 0.2 and abs(y - best_y) <= 0.2):
            return True
    return False


def Himmelblau_Eval(x,y):
    value = (x**2 + y - 11)**2 + (x + y**2 - 7)**2

    if AlreadyFound((x,y), found_minima):
        return 5
    else:
        return value



def rankSort(population):
    population.sort(key=lambda x : Himmelblau_Eval(x[0], x[1]))


def init_population(num_pop):
    ret = []
    for i in range(num_pop):
        x_val = random.choice([-1,1]) * (random.random() * MAX)
        y_val = random.choice([-1,1]) * (random.random() * MAX)
        ret.append([x_val, y_val])
    return ret

def repr(m1, m2, alpha=0.5):
    x = random.uniform(m1[0] - alpha*(m2[0] - m1[0]), m2[0] + alpha*(m2[0] - m1[0]))
    y = random.uniform(m1[1] - alpha*(m2[1] - m1[1]), m2[1] + alpha*(m2[1] - m1[1]))
    if x > MAX:
        x = MAX
    elif x < MIN:
        x = MIN

    if y > MAX:
        y = MAX
    elif y < MIN:
        y = MIN


    return [x, y]


def mutate(m, change=0.01, mutation_rate=0.35):
    if random.random() < mutation_rate:
        sel = 0
        sign = random.choice([1,-1])

        m[sel] += (sign*change)
        if m[sel] > MAX:
            m[sel] = MAX
        elif m[sel] < MIN:
            m[sel] = MIN

    if random.random() < mutation_rate:
        sel = 1
        sign = random.choice([1,-1])

        m[sel] += (sign*change)
        if m[sel] > MAX:
            m[sel] = MAX
        elif m[sel] < MIN:
            m[sel] = MIN
    return m



def selection(population, generation):
    new_gen = []
    rankSort(population)
    elite = population[0:int(len(population) / 3)]
    new_gen += elite
    num = len(new_gen)

    successful = population[0:int(len(population) / 2)]
    while num < POPULATION_NUMBER - int(POPULATION_NUMBER/10):
        m1 = successful[(random.randrange(len(successful)))]
        m2 = successful[(random.randrange(len(successful)))]
        new_gen += [repr(m1, m2)]
        num += 1

    start = len(elite)
    if generation > 1000:
        start = 0
    for i in range(len(elite), len(new_gen)):
        new_gen[i] = mutate(new_gen[i], change=min(0.5, 0.01*generation))

    new_gen += init_population(int(POPULATION_NUMBER/10))


    return new_gen



def SatisfactoryAnswer(best):
    global_minima = [(3.0, 2.0), (-2.805118, 3.131312), (-3.779310, -3.283186), (3.584458, -1.848126)]
    best_x, best_y = best
    for x,y in global_minima:
        if (abs(x - best_x) < .001 and abs(y - best_y) < .001):
            return True
    return False





pop = init_population(POPULATION_NUMBER)
pop2 = init_population(POPULATION_NUMBER)
pop3 = init_population(POPULATION_NUMBER)
pop4 = init_population(POPULATION_NUMBER)
populations = [pop, pop2, pop3, pop4]

rankSort(pop)
best_x, best_y = pop[0]



def NichedEvolution():
    for p in range(len(populations)):
        if p not in settled:
            populations[p] = selection(populations[p], gen)
            rankSort(populations[p])
            best_x, best_y = populations[p][0]
            if SatisfactoryAnswer((best_x, best_y)):
                if not AlreadyFound((best_x, best_y), found_minima):
                    found_minima.append((best_x, best_y))
                    settled.append(p)
                else:
                    populations[p] = init_population(POPULATION_NUMBER)









while len(found_minima) < 4 and gen < 100000:
    NichedEvolution()
    gen += 1
    print(f"GENERATION: {gen} -> {found_minima}")


print(f"FOUND GLOBAL MINIMA: {found_minima}")


