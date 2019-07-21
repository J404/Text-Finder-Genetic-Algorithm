from Brain import Brain


class Sequencer:
    def __init__(self, target):
        self.target = target
        self.brain = Brain(len(target))
        self.fitness = 0

    def calc_fitness(self):
        self.fitness = 0
        score = 0
        for i in range(len(self.target)):
            if self.brain.guess[i] == self.target[i]:
                score += 1

        self.fitness = score / len(self.target)

    def mutate(self):
        self.brain.mutate()

    def show(self):
        print(self.brain.guess)
