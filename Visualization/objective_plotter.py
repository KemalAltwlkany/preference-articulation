import numpy as np
import matplotlib.pyplot as plt
import math as math

fig_num = 1

# S. Huband, 7 recommendations:
# R1.) No Extremal Parameters
# R2.) No Medial Parameters
# R3.) Scalable Number of Parameters
# R4.) Scalable Number of Objectives
# R5.) Dissimilar Parameter Domains
# R6.) Dissimilar Tradeoff Ranges
# R7.) Pareto Optima Known


# noinspection DuplicatedCode
def a1():
    """
    In the work of S. Huband, this test function is labeled "BK1"
    From T.T.Binh, U. Korn - "An evolution strategy for the multiobjective optimization"; page 4/6
    A simple bi-objective problem
        f1(x1, x2) = x1**2 + x2**2
        f2(x1, x2) = (x1-5)**2 + (x2-5)**2
    Region is defined as x1 € [-5, 10] and x2 € [-5, 10]
    Characteristics:
    f1: Separable, Unimodal
    f2: Separable, Unimodal
    Pareto front convex
    R1 - y, R2 - no, R3 - no, R4 - no, R5 - no, R6 - no, R7 - no

    :return:
    """
    # first part plots the entire scatter plot, the grid of the fitness space
    global fig_num
    x1 = np.linspace(-5, 10, 300)
    x2 = np.linspace(-5, 10, 300)
    f1 = []
    f2 = []
    for i in x1:
        for j in x2:
            f1.append(i ** 2 + j ** 2)
            f2.append((i - 5) ** 2 + (j - 5) ** 2)

    plt.figure(fig_num)
    plt.scatter(f1, f2)
    plt.xlabel('f1(x1, x2)')
    plt.ylabel('f2(x1, x2)')
    plt.title('Evaluation of f1(x1, x2), f2(x1, x2)')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    fig_num = fig_num + 1

    # second part plots the Pareto front of the problem
    f1 = x1**2 + x2**2
    f2 = (x1-5)**2 + (x2-5)**2
    plt.plot(f1, f2, linewidth=3.5, linestyle='-', color='r')
    plt.figure(fig_num)
    plt.plot(f1, f2, linewidth=3.5)
    plt.xlabel('f1(x1, x2)')
    plt.ylabel('f2(x1, x2)')
    plt.title('Pareto front of f1(x1, x2), f2(x1, x2)')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    fig_num = fig_num + 1
    plt.show()


# noinspection DuplicatedCode
def a2():
    """
    In the work of S. Huband, this test function is labeled "IM1"
    From: H. Ishibuchi,T. Murata;
    "A multi-objective genetic local search algorithm and its application to flowshop scheduling"
    Test problem 2:
        minimize: f1(x1, x2) 2*sqrt(x1)
            f2(x1, x2) = x1*(1-x2) + 5
            x1 € [1, 4], x2 € [1, 2]
    Interesting problem because of a nonconvex fitness space. Weighted algorithms perform poorly on nonconvex spaces.
    f1 - unimodal
    f2 - unimodal
    R1 - no, R2 - yes, R3 - no, R4 - no, R5 - yes, R6 - yes, R7 - yes
    Fitness space is CONCAVE.

    :return:
    """
    # first part plots the entire scatter plot, the grid of the fitness space
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
    plt.scatter(f1, f2)
    plt.xlabel('f1(x1, x2)')
    plt.ylabel('f2(x1, x2)')
    plt.title('Evaluation of f1(x1, x2), f2(x1, x2)')
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.grid(True)
    fig_num = fig_num + 1

    # second part plots the Pareto front of the problem

    # f1 = 2*np.sqrt(x1)
    # f2 = x1*(1-x2) + 5
    # plt.plot(f1, f2, linewidth=3.5, linestyle='-', color='r')
    # plt.figure(fig_num)
    # plt.plot(f1, f2, linewidth=3.5, linestyle='-', color='b')
    # plt.xlabel('f1(x1, x2)')
    # plt.ylabel('f2(x1, x2)')
    # plt.title('Pareto front of f1(x1, x2), f2(x1, x2)')
    # plt.xlim(0, 5)
    # plt.ylim(0, 5)
    # plt.grid(True)
    # fig_num = fig_num + 1
    plt.show()


#noinspection DuplicatedCode
def a3():
    global fig_num
    x1_space = np.linspace(-5, 5, 200)
    x2_space = np.linspace(-5, 5, 200)
    x3_space = np.linspace(-5, 5, 200)
    f1 = []
    f2 = []
    for x1 in x1_space:
        for x2 in x2_space:
            for x3 in x3_space:
                s1 = -10*math.exp(-0.2*math.sqrt(x1**2 + x2**2)) - 10*math.exp(-0.2*math.sqrt(x2**2+x3**2))
                f1.append(s1)
                s2 = math.pow(math.fabs(x1), 0.8) + math.pow(math.fabs(x2), 0.8) + math.pow(math.fabs(x3), 0.8)
                s3 = math.sin(math.pow(x1, 3)) + math.sin(math.pow(x2, 3)) + math.sin(math.pow(x3, 3))
                f2.append(s2+5*s3)

    plt.figure(fig_num)
    plt.scatter(f1, f2)
    plt.xlabel('f1(x1, x2, x3)')
    plt.ylabel('f2(x1, x2, x3)')
    plt.title('Evaluation of f1(x1, x2, x3), f2(x1, x2, x3)')
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.grid(True)
    fig_num = fig_num + 1
    plt.show()


if __name__ == '__main__':
    a1()
    a2()
    a3()
