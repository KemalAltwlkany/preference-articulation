from LocalSearch.LS_apriori import LocalSearchApriori
from PreferenceArticulation.BenchmarkObjectives import MOO_Problem
from PreferenceArticulation.Solution import Solution
from PreferenceArticulation.Constraints import *
import numpy as np
import matplotlib.pyplot as plt
import random as random

fig_num = 1


def LS_BK1_core(init_sol, delta, max_iter, constraints, weights, M, title):

    # running Local Search on MOO Problem BK1
    problem = MOO_Problem.BK1
    search_alg = LocalSearchApriori(init_sol=init_sol, problem=problem, delta=delta, max_iter=max_iter, constraints=constraints, M=M, weights=weights, n_objectives=2)
    search_history = search_alg.search()
    print('Final solution is: ', search_history[-1])

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
    plt.title('Search history, Local Search, BK1 ' + title)
    plt.xlabel('f1(x1, x2)')
    plt.ylabel('f2(x1, x2)')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()
    fig_num = fig_num + 1


def LS_BK1_variations():
    random.seed(100)
    init_sol = Solution([random.uniform(-5, 10), random.uniform(-5, 10)])
    delta = 0.001
    max_iter = 500
    constraints = [BoundaryConstraint([(-5, 10), (-5, 10)])]
    M = 100

    # A search with equal weights
    weights = [0.5, 0.5]
    LS_BK1_core(init_sol=init_sol, delta=delta, max_iter=max_iter, constraints=constraints, weights=weights, M=M, title='w=[0.5, 0.5]')

    # A search prioritizing the second criteria by a factor of 2
    weights = [0.33, 0.67]
    LS_BK1_core(init_sol=init_sol, delta=delta, max_iter=max_iter, constraints=constraints, weights=weights, M=M, title='w=[0.33, 0.67]')

    # A search prioritizing the first criteria by a factor of 2
    weights = [0.67, 0.33]
    LS_BK1_core(init_sol=init_sol, delta=delta, max_iter=max_iter, constraints=constraints, weights=weights, M=M, title='w=[0.67, 0.33]')


if __name__ == '__main__':
    LS_BK1_variations()
