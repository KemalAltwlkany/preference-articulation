import copy as copy
from Solution import *


class LocalSearch:

    def __init__(self, init_sol=None, objectives=None, delta=None, max_iter=None, constraints=None):
        self.init_sol = init_sol
        self.max_iter = max_iter
        self.objectives = objectives
        self.constraints = constraints
        self.delta = delta

    # function returns a list of vectors containing the first input x's neighborhood.
    # noinspection DuplicatedCode
    def generate_neighborhood(self, x=[], neighborhood=[], current_span=[]):
        if len(x) == 1:
            span1 = list(current_span)
            span1.append(x[0] - self.delta)
            span2 = list(current_span)
            span2.append(x[0])
            span3 = list(current_span)
            span3.append(x[0] + self.delta)
            neighborhood.append(span1)
            neighborhood.append(span2)
            neighborhood.append(span3)
            return neighborhood
        else:
            new_span = list(current_span)
            new_span.append(x[0])
            neighborhood = self.generate_neighborhood(x=x[1:], neighborhood=neighborhood, current_span=new_span)
            new_span[-1] = new_span[-1] - self.delta
            neighborhood = self.generate_neighborhood(x=x[1:], neighborhood=neighborhood, current_span=new_span)
            new_span[-1] = new_span[-1] + 2 * self.delta
            neighborhood = self.generate_neighborhood(x=x[1:], neighborhood=neighborhood, current_span=new_span)
        return neighborhood

    def sort_neighborhood(self, neighborhood):
        pass

    def evaluate_solution(self, sol):
        y = []
        for f in self.objectives:
            y.append(f(sol.x))
        return y

    # WORKS FOR SINGLE OBJECTIVE PROBLEMS ONLY, NEEDS TO BE REWORKED
    @staticmethod
    def compare_solutions(sol1):
        return sol1.y[0]

    def search(self):
        it = 0
        y = self.evaluate_solution(self.init_sol)
        self.init_sol.set_y(y)
        curr_sol = self.init_sol
        while it < self.max_iter:
            it = it + 1
            prev_sol = copy.deepcopy(curr_sol)
            neighborhood_search_space = self.generate_neighborhood(curr_sol.x)
            neighborhood_search_space.remove(curr_sol.x)
            neighborhood_solutions = []

            for x in neighborhood_search_space:
                neighborhood_solutions.append(Solution(x))
                y = self.evaluate_solution(neighborhood_solutions[-1])
                neighborhood_solutions[-1].set_y(y)

            neighborhood_solutions.sort(key=LocalSearch.compare_solutions)
            curr_sol = neighborhood_solutions[0]

            if prev_sol == curr_sol:
                print('Terminating after iteration number', it, ' because local extrema was found')
        print('Terminating because max iterations were exceeded')
        return curr_sol


def f1(x):
    return math.pow(x[0], 2)


def main():
    init_sol = Solution([16])
    delta = 0.1
    max_iter = 500
    objectives = [f1]
    example = LocalSearch(init_sol=init_sol, objectives=objectives, delta=delta, max_iter=max_iter)
    res = example.search()
    print('Result x=', res.x, ' with criteria y=', res.y)


if __name__ == '__main__':
    main()

