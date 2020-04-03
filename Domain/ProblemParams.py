
class ProblemParams:
    def __init__(self, network, method):
        self.network = network
        self.size = len(network)
        self.function = method
