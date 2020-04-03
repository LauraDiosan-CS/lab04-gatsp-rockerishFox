from random import randint

from Domain.Chromosome import Chromosome

class GA:
    def __init__(self, params=None, problParam=None):
        self.params = params
        self.problParams = problParam
        self.population = []

    def initialisation(self):
        for i in range(self.params.populationSize):
            chromo = Chromosome(self.problParams)
            self.population.append(chromo)

    def evaluation(self):
        for chromo in self.population:
            chromo.fitness = self.problParams.function(chromo.representation, self.problParams.network)

    def best_chromosome(self):
        best = self.population[0]
        for chromo in self.population:
            if chromo.fitness < best.fitness:
                best = chromo
        return best

    def worst_chromosome(self):
        worst = self.population[0]
        for chromo in self.population:
            if chromo.fitness > worst.fitness:
                worst = chromo
        return worst

    def selection(self):
        pos1 = randint(0, len(self.population) - 1)
        pos2 = randint(0, len(self.population) - 1)

        fit1 = self.population[pos1].fitness
        fit2 = self.population[pos2].fitness

        if fit1 < fit2:
            return pos1
        else:
            return pos2

    def one_generation_steady_state(self):
        bestOff = Chromosome(self.problParams)

        for _ in range(self.params.populationSize):
            p1 = self.population[self.selection()]
            p2 = self.population[self.selection()]

            off = p1.crossover(p2, self.params.crossoverProb)

            off.mutation()

            off.fitness = self.problParams.function(off.representation, self.problParams.network)

            if off.fitness < bestOff.fitness:
                bestOff = off

        self.population.remove(self.worst_chromosome())
        self.population.append(bestOff)
