from PreferenceArticulation.SearchAlgorithm import SearchAlgorithm
import copy as copy


class TabuSearch(SearchAlgorithm):

    def __init__(self, init_sol=None, problem=None, delta=None, max_iter=None, constraints=None, M=100,
                 tabu_list_max_length=30, max_loops=10):
        super().__init__(init_sol=init_sol, problem=problem, delta=delta, max_iter=max_iter,
                         constraints=constraints, M=M)
        self.max_loops = max_loops    # maximum steps tolerated for the algorithm to run without any significant change in the search occurring
        self.tabu_list = []
        self.tabu_list_max_length = tabu_list_max_length

    # uses abstract methods, so only child classes can invoke this method
    def search(self, verbose=False):
        it = 0
        # algorithm should evaluate initial solution before anything else
        self.init_sol.y = self.evaluate_solution(self.init_sol)
        self.curr_sol = copy.deepcopy(self.init_sol)
        self.search_history.append(copy.deepcopy(self.curr_sol))
        it_without_increment = 0    # number of iterations without any significant change
        while it < self.max_iter:
            it = it + 1
            prev_sol = copy.deepcopy(self.curr_sol)

            self.generate_neighborhood(self.curr_sol)

            # Evaluating the fitness of a solution is costly. It is better to firstly purge the Tabu list
            # and to evaluate the neighborhood afterwards
            # Prone to mistakes. Should verify.
            for tabu_sol in self.tabu_list:
                if tabu_sol in self.neighborhood:
                    self.neighborhood.remove(tabu_sol)

            # Evaluate the individuals now
            self.evaluate_neighborhood()
            self.sort_neighborhood()

            self.curr_sol = self.neighborhood[0]    # new solution becomes the best of the neighborhood
            self.search_history.append(copy.deepcopy(self.curr_sol))
            if prev_sol == self.curr_sol:
                print('Terminating after iteration number', it, ' because local extrema was found')
                return self.search_history

            # remove first 15 elements from tabu list if it is too long
            if len(self.tabu_list) > self.tabu_list_max_length:
                self.tabu_list = self.tabu_list[14:]

            self.tabu_list.append(copy.deepcopy(self.curr_sol))

            if verbose is True:
                print("----------------------------------------------------------")
                print("Iteration number = ", it)
                print("Previous solution, decision variables = ", ["%.3f" % i for i in prev_sol.x])
                print("Previous solution, objectives = ", ["%.3f" % i for i in prev_sol.y])
                print("Current solution, decision variables = ", ["%.3f" % i for i in self.curr_sol.x])
                print("Current solution, objectives = ", ["%.3f" %i for i in self.curr_sol.y])
                # print("First 5 elements of Tabu list = ",  self.tabu_list[:5])
                # print("Last 5 elements of Tabu list = ",  self.tabu_list[-5:])
                print("----------------------------------------------------------")

        print('Terminating because max iterations were exceeded, it = ', it)
        return self.search_history




