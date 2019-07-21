import random


class Brain:
    def __init__(self, length):
        self.length = length
        self.chars = "abcdefghijklmnopqrstuvwxyz '.,"
        self.guess = ""
        self.create_instructions()

    def create_instructions(self):
        for i in range(self.length):
            rand = random.randint(0, len(self.chars) - 1)
            self.guess += self.chars[rand]

    def mutate(self):
        new_guess = ""
        for i in range(self.length):
            rand = random.uniform(0, 1)
            new_letter = self.guess[i]
            if rand < 0.01:
                new_letter = self.chars[random.randint(0, len(self.chars) - 1)]
            new_guess += new_letter
        self.guess = new_guess

    @staticmethod
    def crossover(mid, parent_a, parent_b):
        new_guess = ""
        for i in range(len(parent_b.target)):
            if i < mid:
                new_guess += parent_a.brain.guess[i]
            else:
                new_guess += parent_b.brain.guess[i]
        return new_guess


