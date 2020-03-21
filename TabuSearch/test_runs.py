from TabuSearch.TS_apriori import TabuSearchApriori
from PreferenceArticulation.Solution import Solution
from PreferenceArticulation.BenchmarkObjectives import MOO_Problem
import numpy as np
import matplotlib.pyplot as plt
import random as random
import math as math

fig_num = 1


def TS_BK1():

    # running TabuSearch on MOO Problem BK1
    problem = MOO_Problem.BK1
    init_sol = Solution([-2, 6])
    delta = 0.01
    max_iter = 5000
    constraints = None
    weights = [1, 1]
    n_objectives = 2
    search_alg = TabuSearchApriori(init_sol=init_sol, problem=problem, delta=delta, max_iter=max_iter, constraints=constraints, tabu_list_max_length=30, weights=weights, n_objectives=n_objectives)
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
    plt.title('Search history, Tabu Search, BK1')
    plt.xlabel('f1(x1, x2)')
    plt.ylabel('f2(x1, x2)')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()
    fig_num = fig_num + 1


def TS_IM1():
    # This example perfectly demonstrates the weakness of weighted search algorithms for MOOPs. For random.seed(2)
    # and random.seed(16) the algorithm performs completely different.
    # running TabuSearch on MOO Problem IM1
    problem = MOO_Problem.IM1
    random.seed(16)
    init_sol = Solution([random.uniform(1, 4), random.uniform(1, 2)])
    delta = 0.001
    max_iter = 500
    constraints = None
    weights = [1, 1]
    n_objectives = 2
    search_alg = TabuSearchApriori(init_sol=init_sol, problem=problem, delta=delta, max_iter=max_iter, constraints=constraints, tabu_list_max_length=30, weights=weights, n_objectives=n_objectives)
    search_history = search_alg.search(verbose=False)

    # plotting the results
    global fig_num
    x1 = np.linspace(1, 4, 300)
    x2 = np.linspace(1, 2, 300)
    f1 = []
    f2 = []
    for i in x1:
        for j in x2:
            f1.append(2*math.sqrt(i))
            f2.append(i*(1-j) + 5)

    plt.figure(fig_num)
    plt.scatter(f1, f2, s=1.0)

    f1 = []
    f2 = []
    for sol in search_history:
        f1.append(sol.y[0])
        f2.append(sol.y[1])
    plt.plot(f1, f2, linewidth=3.5, linestyle='-', color='r')
    plt.title('Search history, Tabu Search, IM1')
    plt.xlabel('f1(x1, x2)')
    plt.ylabel('f2(x1, x2)')
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.grid(True)
    plt.show()
    fig_num = fig_num + 1


if __name__ == '__main__':
    # TS_BK1()
    TS_IM1()