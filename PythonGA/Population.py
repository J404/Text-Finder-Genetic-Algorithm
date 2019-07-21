from Sequencer import Sequencer
import random
from Brain import Brain


class Population:
    def __init__(self, size, target):
        self.size = size
        self.pop = []
        self.target = target
        for i in range(size):
            self.pop.append(Sequencer(self.target))
        self.fitness_sum = 0
        self.best_ind = 0
        self.gen = 0

    def calculate_fitness(self):
        for s in self.pop:
            s.calc_fitness()

    def calculate_fitness_sum(self):
        self.fitness_sum = 0
        for s in self.pop:
            self.fitness_sum += s.fitness

    def get_best(self):
        max_fit = 0
        max_fit_i = 0
        for i in range(len(self.pop)):
            if self.pop[i].fitness > max_fit:
                max_fit = self.pop[i].fitness
                max_fit_i = i
        self.best_ind = max_fit_i

    def select_parent(self):
        running_sum = 0
        rand = random.uniform(0, self.fitness_sum)

        for s in self.pop:
            running_sum += s.fitness
            if rand < running_sum:
                return s

    def natural_selection(self):
        new_gen = []
        self.calculate_fitness_sum()
        self.get_best()

        new_gen.append(self.pop[self.best_ind])
        parent_b = self.select_parent()
        new_guess = Brain.crossover(random.randint(0, len(self.target)), self.pop[self.best_ind], parent_b)
        new_gen[0].brain.guess = new_guess

        for i in range(1, self.size):
            parent_a = self.select_parent()
            parent_b = self.select_parent()
            new_gen.append(Sequencer(self.target))
            new_gen[i].brain.guess = Brain.crossover(random.uniform(0, len(self.target)), parent_a, parent_b)
        self.pop = new_gen
        self.gen += 1

    def mutate_babies(self):
        for s in self.pop:
            s.mutate()

    def cull(self):
        for s in self.pop:
            if s.fitness < self.pop[self.best_ind].fitness:
                s.mutate()

    def show_best(self):
        print(self.pop[self.best_ind].brain.guess + " " + str(self.gen))
