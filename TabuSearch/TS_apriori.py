from TabuSearch.TS import TabuSearch


class TabuSearchApriori(TabuSearch):

    weights = [1, 1]
    n_objectives = 2

    def __init__(self, init_sol=None, problem=None, delta=None, max_iter=None, constraints=None, M=100,
                 tabu_list_max_length=30, weights=None, n_objectives=None, max_loops=10):
        super().__init__(init_sol=init_sol, problem=problem, delta=delta, max_iter=max_iter, constraints=constraints,
                         M=M, tabu_list_max_length=tabu_list_max_length, max_loops=max_loops)
        TabuSearchApriori.weights = weights
        TabuSearchApriori.n_objectives = n_objectives

    def sort_neighborhood(self):
        self.neighborhood.sort(key=TabuSearchApriori.compute_fitness)

    @staticmethod
    def compute_fitness(sol):
        """
        In apriori articulation, a full order can be introduced within the set of solutions being considered.
        The parameter/key which is used to establish full order is called the fitness of the solution.
        :param sol:
        :return:
        """
        fit = 0
        for i in range(TabuSearchApriori.n_objectives):
            fit = fit + TabuSearchApriori.weights[i] * sol.y[i]
        return fit

