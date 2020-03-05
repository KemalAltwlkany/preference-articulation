class LocalSearch:
    def __init__(self, x0=None, objectives=None, delta=None, max_iter=None, constraints=None):
        self.x0 = x0
        self.delta = delta
        self.max_iter = max_iter
        self.objectives = objectives
        self.constraints = constraints

    def generate_neighborhood(self, x):


    def generate_neighborhood(self, x, neighborhood=[]):
        if len(x) == 1:
            neighborhood.append(x-self.delta)
            neighborhood.append(x)
            neighborhood.append(x+self.delta)
        else:

        # x is of type solution
        #Should return all permutations of variable x