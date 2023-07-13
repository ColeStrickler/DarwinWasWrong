import math
import random

import numpy as np
from math import *

MIN = -512.0
MAX = 512.0

POPULATION_NUMBER = 50

def EggHolder_Eval(x,y):
    return (-1*(y+47))*sin(sqrt(abs((x/2) + (y+47)))) - (x * sin(sqrt(abs(x - (y+47)))))

def rankSort(population):
    population.sort(key=lambda x : EggHolder_Eval(x[0], x[1]))


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
    if x > 512:
        x = 512
    elif x < -512:
        x = -512

    if y > 512:
        y = 512
    elif y < -512:
        y = -512


    return [x, y]


def mutate(m, change=5, mutation_rate=0.35):
    if random.random() < mutation_rate:
        sel = 0
        sign = random.choice([1,-1])

        m[sel] += (sign*change)
        if m[sel] > 512:
            m[sel] = 512
        elif m[sel] < -512:
            m[sel] = -512

    if random.random() < mutation_rate:
        sel = 1
        sign = random.choice([1,-1])

        m[sel] += (sign*change)
        if m[sel] > 512:
            m[sel] = 512
        elif m[sel] < -512:
            m[sel] = -512
    return m



def selection(population, generation):
    new_gen = []
    rankSort(population)
    elite = population[0:int(len(population) / 3)]
    new_gen += elite
    num = len(new_gen)

    successful = population[0:int(len(population) / 2)]
    while num < POPULATION_NUMBER - 2:
        m1 = successful[(random.randrange(len(successful)))]
        m2 = successful[(random.randrange(len(successful)))]
        new_gen += [repr(m1, m2)]
        num += 1

    start = len(elite)
    if generation > 1000:
        start = 0
    for i in range(len(elite), len(new_gen)):
        new_gen[i] = mutate(new_gen[i], change=min(150, 0.1* generation))

    new_gen += init_population(2)


    return new_gen




pop = init_population(POPULATION_NUMBER)
rankSort(pop)
best_x, best_y = pop[0]
#print(pop)
#print(pop[0], pop[1])
#print(repr(pop[0], pop[1]))



gen = 0

while (abs(512 - best_x) > .01 or abs(404.23 - best_y) > .01) and gen < 100000:
    pop = selection(pop, gen)
    rankSort(pop)
    best_x, best_y = pop[0]
    gen += 1
    print(f"GENERATION: {gen} -> Best X: {best_x}, Best Y: {best_y}")




