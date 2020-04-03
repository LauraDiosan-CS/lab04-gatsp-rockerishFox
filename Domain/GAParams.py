
class GAParams:
    def __init__(self, popSize, noOfGen, crossP, mutP):
        self.populationSize = popSize
        self.noOfGenerations = noOfGen
        self.crossoverProb = crossP
        self.mutationProb = mutP