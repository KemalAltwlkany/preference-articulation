from LocalSearch.LocalSearch import LocalSearch


class LocalSearchApriori(LocalSearch):
    """
    Implements the apriori articulation of preferences type of LocalSearch. Apriori preferences are dealt with by
    simply aggregating all the objective functions into one objective function, optionally weighted. If no vector
    of weights is passed then it's assumed it's a vector of 1's, i.e. w[i] = 1, for every i.
    """
    def __init__(self, init_sol=None, objectives=None, delta=None, max_iter=None, constraints=None, weights=None):
        super().__init__(init_sol, objectives, delta, max_iter, constraints)
        self.weights = weights
        if weights is None:
            self.weights = [1]*len(self.objectives)  # in case no weights have been specified, use unity weights

    def sort_neighborhood(self):
        """In apriori articulation the set of objective functions is aggregated into one function, effectively making
        the multi-objective optimization problem (MOOP) a single-objective optimization problem (SOOP).
        Therefore, sorting the neighborhood is done by passing a key function to pythons built-in sort function.
        The key function simply performs the aggregation.
        """
        self.neighborhood.sort(key=LocalSearchApriori.compute_fitness)

    def compute_fitness(self, sol):
        """
        In apriori articulation, a full order can be introduced within the set of solutions being considered.
        The parameter/key which is used to establish full order is called the fitness of the solution.
        :param sol: 
        :return:
        """
        fit = 0
        for i in range(len(self.objectives)):
            fit = fit + self.weights[i] * sol.y[i]
        return fit

