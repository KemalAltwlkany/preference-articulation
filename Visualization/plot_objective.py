import numpy as np
import matplotlib.pyplot as plt
from PreferenceArticulation.BenchmarkObjectives import *


def bi_objective_scatter_plot(f1, f2, x, title="sample", xlabel=None, ylabel=None, ):
    fig = plt.figure()
    f1_values = []
    f2_values = []
    for xi in x:
        f1_values.append(f1(xi))
        f2_values.append(f2(xi))
    plt.scatter(f1_values, f2_values)
    plt.show()


def example1():
    """
    Basically plots the envelope/borderline of a meshgrid. In order to plot, uses linspace combinations.
    :return:
    """
    x = np.linspace((0, 0), (10, 10), 1000)
    bi_objective_scatter_plot(Objectives_2D.f1, Objectives_2D.f2, x)


def example2():
    """
    Plots the entire meshgrid, of x,y. A few extra operations have been added to make this more compatible with my
    BenchmarkObjectives class.
    :return:
    """
    x, y = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
    x, y = x.flatten(), y.flatten()
    x, y = np.reshape(x, (10000, 1)), np.reshape(y, (10000, 1))
    x = np.concatenate((x, y), axis=1)
    bi_objective_scatter_plot(Objectives_2D.f1, Objectives_2D.f2, x)


if __name__ == '__main__':
    example1()
    example2()

