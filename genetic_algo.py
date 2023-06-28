import math
import time
import random
import pygame as p


class Food():
    def __init__(self, x, y, pygame, screen):
        self.x = x
        self.y = y
        self.size = 4
        self.pygame = pygame
        self.screen = screen
        self.rect = self.pygame.Rect(x, y, self.size, self.size)
        self.consumed = False

    def consume(self):
        self.consumed = True

    def perform_action(self):
        return

    def draw(self):
        if self.consumed:
            return
        p.draw.rect(self.screen, self.pygame.Color("yellow"), self.rect)

class Darwin():
    def __init__(self, width, height, mutation_rate, pygame, screen, dna_len=1000, prey_count=100, predator_count=25, trapper_count=25):
        self.actions = ["0", "1", "2", "3"]
        self.prey_count = prey_count
        self.predator_count = predator_count
        self.trapper_count = trapper_count
        self.dna_len = dna_len
        self.width = width
        self.height = height
        self.food = []
        self.prey = []
        self.predators = []
        self.trappers = []
        self.pygame = pygame
        self.screen = screen
        self.mutation_rate = mutation_rate
        self.prey_start = (50, 50)
        self.predator_start = (width/2, height/2)
        self.trapper_start = (width - 300, height - 300)
        self.numGenerations = 0
        # Generate Initial Populations
        self.genFoodLocations()
        self.genInitialPrey()
        self.genInitialPredators()
        self.genInitialTrappers()


    def mutate(self, DNA, trapper=False):
        ret = ""
        num = 3
        if trapper:
            num += 1
        for i in range(len(DNA)):
            mutate = random.random() < self.mutation_rate
            if mutate:
                new_action = random.randint(0, num)
                ret += f"{new_action}"
            else:
                ret += DNA[i]
        return ret

    def genInitialPrey(self):
        for i in range(self.prey_count):
            dna = ""
            for j in range(self.dna_len):
                sel = random.randint(0, 3)
                dna += self.actions[sel]
            prey = Prey(self.prey_start[0], self.prey_start[1], self.pygame, self.screen, DNA=dna)
            self.prey.append(prey)



    def genPrey(self, dna_list):
        for d in dna_list:
            prey = Prey(self.prey_start[0], self.prey_start[1], self.pygame, self.screen, DNA=d)
            self.prey.append(prey)

    def genInitialTrappers(self):
        actions = ["0", "1", "2", "3", "4"]
        for i in range(self.trapper_count):
            dna = ""
            for j in range(self.dna_len):
                sel = round(random.random() * 4 - 0.45)
                dna += actions[sel]
            prey = Trapper(self.trapper_start[0], self.trapper_start[1], self.pygame, self.screen, DNA=dna)
            self.trappers.append(prey)

    def genTrappers(self, dna_list):
        for d in dna_list:
            trapper = Trapper(self.trapper_start[0], self.trapper_start[1], self.pygame, self.screen, DNA=d)
            self.trappers.append(trapper)

    def genPredators(self, dna_list):
        for d in dna_list:
            pred = Predator(self.predator_start[0], self.predator_start[1], self.pygame, self.screen, DNA=d)
            self.predators.append(pred)


    def genInitialPredators(self):
        for i in range(self.predator_count):
            dna = ""
            for j in range(self.dna_len):
                sel = random.randint(0, 3)
                dna += self.actions[sel]
            prey = Predator(self.predator_start[0], self.predator_start[1], self.pygame, self.screen, DNA=dna)
            self.predators.append(prey)


    def rankFitness(self):
        self.prey.sort(key=lambda x: x.score, reverse=True)
        self.predators.sort(key=lambda x: x.score, reverse=True)


    def reproduce(self, m1, m2):
        # splice dna at random point and generate two new offspring
        dna1 = m1.DNA
        dna2 = m2.DNA
        splice_location = random.randint(5,  len(dna1) - 5)
        new_dna1 = dna1[0: splice_location] + dna2[splice_location:]
        new_dna2 = dna2[0: splice_location] + dna1[splice_location:]
        return [new_dna1, new_dna2]

    def evolvePrey(self):
        self.rankFitness()
        dna_pool = []
        added = 0
        for i in range(0, int(len(self.prey) / 5)): # keep top 20%
            dna_pool.append(self.prey[i].DNA)
            added += 1
        successful = self.prey[0:int(len(self.prey)/4)] # choose top 25% for reproduction
        while added < self.prey_count:
            m1 = successful[(random.randrange(len(successful)))]
            m2 = successful[(random.randrange(len(successful)))]
            dna_pool += self.reproduce(m1, m2)
            added += 1
        for i in range(int(len(self.prey) / 5), len(dna_pool)):
            dna_pool[i] = self.mutate(dna_pool[i]) # apply mutations only to offspring created by reproduction
        self.prey.clear()
        self.genPrey(dna_list=dna_pool)


    def evolveTrappers(self):
        self.rankFitness()
        dna_pool = []
        added = 0
        for i in range(0, int(len(self.trappers) / 8)):
            dna_pool.append(self.trappers[i].DNA)
            added += 1
        successful = self.trappers[0:int(len(self.trappers)/5)]

        while added < self.trapper_count:
            m1 = successful[(random.randrange(len(successful)))]
            m2 = successful[(random.randrange(len(successful)))]
            dna_pool += self.reproduce(m1, m2)
            added += 1
        for i in range(int(len(self.predators) / 2), len(dna_pool)):
            dna_pool[i] = self.mutate(dna_pool[i], trapper=True)
        self.trappers.clear()
        self.genTrappers(dna_list=dna_pool)


    def evolvePredators(self):
        self.rankFitness()
        dna_pool = []
        added = 0
        for i in range(0, int(len(self.predators) / 5)):
            dna_pool.append(self.predators[i].DNA)
            added += 1
        successful = self.predators[0:int(len(self.predators)/3)]

        while added < self.predator_count:
            m1 = successful[(random.randrange(len(successful)))]
            m2 = successful[(random.randrange(len(successful)))]
            dna_pool += self.reproduce(m1, m2)
            added += 1
        for i in range(int(len(self.predators) / 2), len(dna_pool)):
            dna_pool[i] = self.mutate(dna_pool[i])
        self.predators.clear()
        self.genPredators(dna_list=dna_pool)


    def runCycle(self, draw=True):
        for f in self.food:
            if draw:
                f.draw()
        check = self.prey[0]

        if check.done_actions < self.dna_len:
            for prey in self.prey:
                prey.perform_action()
                if draw:
                    prey.draw()
                for f in self.food:
                    if f.rect.colliderect(prey.rect):
                        prey.consume_food(f)
            for predator in self.predators:
                predator.perform_action()
                if draw:
                    predator.draw()
                for p in self.prey:
                    if p.rect.colliderect(predator.rect):
                        predator.consume_food(p)
            for t in self.trappers:
                t.perform_action()
                if draw:
                    t.draw()
                for trap in t.traps:
                    if draw:
                        trap.draw()
                    for p in self.prey:
                        if p.rect.colliderect(trap.rect):
                            trap.snare(p)
                    for pred in self.predators:
                        if pred.rect.colliderect(trap.rect):
                            trap.snare(pred)



        else:
            self.evolvePrey()
            self.evolvePredators()
            self.evolveTrappers()
            self.reset()
            self.numGenerations += 1
            print(f"GENERATION {self.numGenerations}")




    def evolve(self):
        self.rankFitness()


    def reset(self):
        for f in self.food:
            f.consumed = False

    def genFoodLocations(self):
        h = 30
        while h < self.height:
            x = 30
            while x < self.width:
                self.food.append(Food(x, h, self.pygame, self.screen))
                x += 30
            h += 30






class Trapper():
    def __init__(self, x, y, pygame, screen, DNA):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.screen = screen
        self.screen_size = self.screen.get_size()
        self.size = 6
        self.rect = self.pygame.Rect(x, y, self.size, self.size)
        self.num_actions = len(DNA)
        self.done_actions = 0
        self.score = 0
        self.DNA = DNA
        self.type = "P"
        self.dead = False
        self.traps = []
        self.traps_left = 15

    def draw(self):
        p.draw.rect(self.screen, self.pygame.Color("blue"), self.rect)

    def layTrap(self):
        if self.traps_left > 0:
            trap = Trap(self.x, self.y, self, self.pygame, self.screen)
            self.traps.append(trap)
            self.traps_left -= 1

    def perform_action(self):
        if self.done_actions < self.num_actions:
            action = self.DNA[self.done_actions]
            if action == "0" and self.x + 8 <= self.screen_size[0]:
                self.x += 10
            elif action == "1" and self.x - 8 >= 0:
                self.x -= 10
            elif action == "2" and self.y + 8 <= self.screen_size[1]:
                self.y += 10
            elif action == "3" and self.y - 8 >= 0:
                self.y -= 10
            elif action == "4":
                self.layTrap()
            self.rect = self.pygame.Rect(self.x, self.y, self.size, self.size)
        self.done_actions += 1



class Trap():
    def __init__(self, x, y, parent, pygame, screen):
        self.x = x
        self.pygame = pygame
        self.screen = screen
        self.y = y
        self.size = 3
        self.parent = parent
        self.used = False
        self.rect = self.pygame.Rect(x, y, self.size, self.size)

    def draw(self):
        if self.used:
            return
        p.draw.rect(self.screen, self.pygame.Color("black"), self.rect)

    def snare(self, victim):
        if not victim.dead:
            victim.die()
            victim.score = 0
            self.parent.score += 1
            self.used = True





class Predator():
    def __init__(self, x, y, pygame, screen, DNA):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.screen = screen
        self.screen_size = self.screen.get_size()
        self.size = 6
        self.rect = self.pygame.Rect(x, y, self.size, self.size)
        self.num_actions = len(DNA)
        self.done_actions = 0
        self.score = 0
        self.DNA = DNA
        self.type = "P"
        self.dead = False

    def draw(self):
        if self.dead:
            return
        p.draw.rect(self.screen, self.pygame.Color("red"), self.rect)

    def perform_action(self):
        if self.done_actions < self.num_actions:
            action = self.DNA[self.done_actions]
            if action == "0" and self.x + 8 <= self.screen_size[0]:
                self.x += 4
            elif action == "1" and self.x - 8 >= 0:
                self.x -= 4
            elif action == "2" and self.y + 8 <= self.screen_size[1]:
                self.y += 4
            elif action == "3" and self.y - 8 >= 0:
                self.y -= 4
            self.rect = self.pygame.Rect(self.x, self.y, self.size, self.size)
        self.done_actions += 1

    def die(self):
        self.dead = True

    def consume_food(self, food):
        if food.dead:
            return
        food.dead = True
        food.score = 0
        self.score += 1
        self.size += 2
        self.rect = self.pygame.Rect(self.x, self.y, self.size, self.size)


class Prey():
    def __init__(self, x, y, pygame, screen, DNA):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.screen = screen
        self.screen_size = self.screen.get_size()
        self.size = 4
        self.rect = self.pygame.Rect(x, y, self.size, self.size)
        self.dead = False
        self.num_actions = len(DNA)
        self.done_actions = 0
        self.score = 0
        self.DNA = DNA

    def draw(self):
        if self.dead:
            return
        p.draw.rect(self.screen, self.pygame.Color("green"), self.rect)

    def die(self):
        self.dead = True

    def perform_action(self):
        if self.done_actions < self.num_actions:
            action = self.DNA[self.done_actions]
            if action == "0" and self.x + 8 <= self.screen_size[0]:
                self.x += 8
            elif action == "1" and self.x - 8 >= 0:
                self.x -= 8
            elif action == "2" and self.y + 8 <= self.screen_size[1]:
                self.y += 8
            elif action == "3" and self.y - 8 >= 0:
                self.y -= 8
            self.rect = self.pygame.Rect(self.x, self.y, self.size, self.size)
        self.done_actions += 1

    def consume_food(self, food):
        if food.consumed or self.dead:
            return
        food.consume()
        self.score += 1
        self.size += 1
        self.rect = self.pygame.Rect(self.x, self.y, self.size, self.size)

