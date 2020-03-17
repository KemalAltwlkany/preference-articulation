import numpy as np
import matplotlib.pyplot as plt

fig_num = 1


def a1():
    """
    From T.T.Binh, U. Korn - "An evolution strategy for the multiobjective optimization"; page 4/6
    A simple bi-objective problem
        f1(x1, x2) = x1**2 + x2**2
        f2(x1, x2) = (x1-5)**2 + (x2-5)**2
    Region is defined as x1 € [-5, 10] and x2 € [-5, 10]
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

    plt.figure(fig_num)
    f1 = x1**2 + x2**2
    f2 = (x1-5)**2 + (x2-5)**2
    plt.plot(f1, f2, linewidth=3.5)
    plt.xlabel('f1(x1, x2)')
    plt.ylabel('f2(x1, x2)')
    plt.title('Pareto front of f1(x1, x2), f2(x1, x2)')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    fig_num = fig_num + 1
    plt.show()


def a2():
    """
    From: H. Ishibuchi,T. Murata;
    "A multi-objective genetic local search algorithm and its application to flowshop scheduling"
    :return:
    """



if __name__ == '__main__':
    a1()

