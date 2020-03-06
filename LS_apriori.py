from LocalSearch import *


class LocalSearchApriori(LocalSearch):
    """
    Implements the apriori articulation of preferences type of LocalSearch. Apriori preferences are dealt with by
    simply aggregating all the objective functions into one objective function, optionally weighted. If no vector
    of weights is passed then it's assumed it's a vector of 1's, i.e. w[i] = 1, for every i.
    """
    def __init__(self, init_sol=None, objectives=None, delta=None, max_iter=None, constraints=None, weights=None):
        super().__init__(init_sol, objectives, delta, max_iter, constraints)
        if weights is None:
            weights = [1]*len(self.objectives)

    def