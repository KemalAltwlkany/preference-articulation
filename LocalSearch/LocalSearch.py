import copy as copy
from PreferenceArticulation.SearchAlgorithm import *


class LocalSearch(SearchAlgorithm):

    def __init__(self, init_sol=None, objectives=None, delta=None, max_iter=None, constraints=None):
        super().__init__(init_sol, objectives, delta, max_iter, constraints)

    # uses abstract methods, so only child classes can invoke this method
    def search(self):
        it = 0
        # algorithm should evaluate initial solution before anything else
        self.init_sol.y = self.evaluate_solution(self.init_sol)
        self.curr_sol = copy.deepcopy(self.init_sol)
        while it < self.max_iter:
            it = it + 1
            prev_sol = copy.deepcopy(self.curr_sol)

            self.generate_neighborhood(self.curr_sol)
            self.evaluate_neighborhood()
            self.sort_neighborhood()

            self.curr_sol = self.neighborhood[0]  # new solution becomes the best of the neighborhood

            if prev_sol == self.curr_sol:
                print('Terminating after iteration number', it, ' because local extrema was found')
                return self.curr_sol

        print('Terminating because max iterations were exceeded')
        return self.curr_sol

