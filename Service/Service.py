from Domain.Chromosome import Chromosome
from Domain.GA import GA
from Domain.GAParams import GAParams
from Domain.ProblemParams import ProblemParams
from Utils import read_graph_from_file, get_route_length


class Service:

    def __init__(self, fileName):
        self.__file = fileName
        self.__gaParameters = GAParams(10, 100, 0.7, 0.15)
        self.__probParameters = 0

    def solve(self):
        graph = read_graph_from_file(self.__file)

        self.__probParameters = ProblemParams(graph, get_route_length)

        ga = GA(self.__gaParameters, self.__probParameters)
        ga.initialisation()
        ga.evaluation()

        best = Chromosome(self.__probParameters)

        for generation in range(self.__gaParameters.noOfGenerations):
            ga.one_generation_steady_state()

            bestChromo = ga.best_chromosome()
            print('Generatia ' + str(
                generation) + ' are cel mai bun cromozom:' + str(best.representation) + ' cu fitness ' + str(
                bestChromo.fitness))
            if bestChromo.fitness < best.fitness:
                best = bestChromo


        print(best.representation)

        print(get_route_length(best.representation, self.__probParameters.network))
