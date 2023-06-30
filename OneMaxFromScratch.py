import random
import sys

POPULATION = 200
LEN = 500
MAX = LEN


def init(num_pop, len):
    ret = []
    for i in range(num_pop):
        individual = ""
        for j in range(len):
            individual += f"{random.randint(0,1)}"
        ret.append(individual)
    return ret


def mutate(dna_string, mut_rate=0.02):
    ret = ""
    for c in dna_string:
        if random.random() <= mut_rate:
            if c == "1":
                ret += "0"
            else:
                ret += "1"
        else:
            ret += c
    return ret


def fitness_val(dna):
    ret = 0
    for i in dna:
        if i == "1":
            ret += 1
    return ret





def rankFitness(population):
    population.sort(key=lambda x: fitness_val(x), reverse=True)

def repr(dna1, dna2):
    new_dna1 = ""
    new_dna2 = ""
    for i in range(len(dna1)):
        if i % 2 == 0:
            new_dna1 += dna1[i]
            new_dna2 += dna2[i]
        else:
            new_dna1 += dna2[i]
            new_dna2 += dna1[i]

    return [new_dna1, new_dna2]


def evolve(population):
    new_gen = []
    elite_num = int(len(population) / 5)
    total_num = len(population)
    successful = population[0:int(len(population) / 3)]
    i = 0
    for i in range(elite_num):
        new_gen.append(population[i])
        i += 1

    while i < total_num:
        m1 = successful[(random.randrange(len(successful)))]
        m2 = successful[(random.randrange(len(successful)))]
        new_gen += repr(m1, m2)
        i += 2

    for i in range(elite_num, total_num):
        new_gen[i] = mutate(new_gen[i])

    return new_gen


pop = init(POPULATION, LEN)
print(f"Initial Population: {pop}\n\n")
best = 0
generations = 0
while True:
    rankFitness(pop)
    best = fitness_val(pop[0])
    if best == MAX:
        print(f"\n\nFINISHED = GENERATION: {generations}, BEST: {best}")
        print(f"Final Population: {pop}")
        break
    print(f"GENERATION: {generations}, BEST: {best}")
    pop = evolve(pop)
    generations += 1



