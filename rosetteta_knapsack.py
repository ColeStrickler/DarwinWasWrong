

# This is a classic example of the knapsack problem. We are attempting to maximize the value of the items
# put into a bag while keeping the total weight under the capacity
import random
from matplotlib import pyplot as plt
items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )
CAPACITY = 400 # (item_name, weight, value)
LEN = len(items)
POPULATION_SIZE = 1000


def getFitnessValue(dna):
    ret = 0
    for i in range(len(dna)):
        if dna[i] == "1":
            ret += items[i][2]
    if get_weight(dna) > CAPACITY:
        return 0
    return ret


def get_weight(dna):
    ret = 0
    for i in range(len(dna)):
        if dna[i] == "1":
            ret += items[i][1]
    return ret


def init(pop_size, length):
    ret = []
    for i in range(pop_size):
        curr_weight = 0
        individual = ""
        for j in range(length):
            num = random.randint(0,1)
            weight = items[num][1]
            if curr_weight + weight <= 400:
                individual += f"{num}"
                curr_weight += weight
            else:
                individual += "0"
        ret.append(individual)
    return ret




def mutate(dna_string, mut_rate=0.02):
    ret = ""
    current_weight = get_weight(dna_string)
    for i in range(len(dna_string)):
        if random.random() <= mut_rate:
            if dna_string[i] == "1":
                ret += "0"
                current_weight -= items[i][1]
            elif current_weight + items[i][1] < 400:
                ret += "1"
                current_weight += items[i][1]
        else:
            ret += dna_string[i]
    return ret


def repr(dna1, dna2):
    new_dna1 = ""
    new_dna2 = ""
    splice_location = random.randint(0, len(dna1) - 1)
    new_dna1 = dna1[0: splice_location] + dna2[splice_location:]
    new_dna2 = dna2[0: splice_location] + dna1[splice_location:]

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


def calcAvg(population):
    total = 0
    for i in population:
        total += getFitnessValue(i)
    return total / len(population)

def rankFitness(population):
    population.sort(key=lambda x: getFitnessValue(x), reverse=True)




pop = init(POPULATION_SIZE, LEN)
print(f"Initial Population: {pop}\n\n")
best = 0
generations = 0
mean_vals = []
max_vals = []

while True:
    rankFitness(pop)
    best = getFitnessValue(pop[0])
    mean = calcAvg(pop)
    max_vals.append(best)
    mean_vals.append(mean)
    if generations > 50:
        print(f"\n\nFINISHED = GENERATION: {generations}, BEST: {best}, AVERGAGE: {calcAvg(pop)}")
        print(f"Final Population: {pop}")
        break
    print(f"GENERATION: {generations}, BEST: {best}")
    pop = evolve(pop)
    generations += 1



plt.plot(max_vals, color='red')
plt.plot(mean_vals, color='green')
plt.xlabel('Generation')
plt.ylabel('Max/Mean')

plt.title('Max and Average fitness over Generations')
plt.show()