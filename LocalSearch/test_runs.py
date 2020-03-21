from LocalSearch.LS_apriori import LocalSearchApriori
from PreferenceArticulation.BenchmarkObjectives import MOO_Problem
from PreferenceArticulation.Solution import Solution
import numpy as np
import matplotlib.pyplot as plt


fig_num = 1


def LS_BK1():

    # running Local Search on MOO Problem BK1
    problem = MOO_Problem.BK1
    init_sol = Solution([-2, 6])
    delta = 0.01
    max_iter = 5000
    constraints = None
    weights = [1, 1]
    n_objectives = 2
    search_alg = LocalSearchApriori(init_sol=init_sol, problem=problem, delta=delta, max_iter=max_iter, constraints=constraints, weights=weights, n_objectives=n_objectives)
    search_history = search_alg.search()

    # plotting the results
    global fig_num
    x1 = np.linspace(-5, 10, 300)
    x2 = np.linspace(-5, 10, 300)
    f1 = []
    f2 = []
    for i in x1:
        for j in x2:
            f1.append(i ** 2 + j ** 2)
            f2.append((i - 5) ** 2 + (j - 5) ** 2)
    plt.figure()
    plt.scatter(f1, f2, s=1.0)

    f1 = []
    f2 = []
    for sol in search_history:
        f1.append(sol.y[0])
        f2.append(sol.y[1])
    plt.plot(f1, f2, linewidth=3.5, linestyle='-', color='r')
    plt.title('Search history, Local Search, BK1')
    plt.xlabel('f1(x1, x2)')
    plt.ylabel('f2(x1, x2)')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()
    fig_num = fig_num + 1


if __name__ == '__main__':
    LS_BK1()
