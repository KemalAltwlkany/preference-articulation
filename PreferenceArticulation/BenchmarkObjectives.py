import math as math


class MOO_Problem:
    """
    Class is never to be instantiated in the first place, its just a wrapper to keep all the benchmark functions used
    in one nice class, which should be used as static functions.
    """

    @staticmethod
    def quadratic(x):
        summ = 0
        for i in x:
            summ = summ + math.pow(i, 2)
        return summ

    @staticmethod
    def f1(x):
        """ B"""
        pass

    @staticmethod
    def BK1(x):
        """
        The BK1 test problem.
        In the work of S. Huband, this test problem is labeled "BK1"
        From T.T.Binh, U. Korn - "An evolution strategy for the multiobjective optimization"; page 4/6
        A simple bi-objective problem
            f1(x1, x2) = x1**2 + x2**2
            f2(x1, x2) = (x1-5)**2 + (x2-5)**2
        Region is defined as x1 € [-5, 10] and x2 € [-5, 10]
        Characteristics:
        f1: Separable, Unimodal
        f2: Separable, Unimodal
        Pareto front convex
        The Pareto front is defined for x1 € [0, 5] and x2 € [0,5].
        This is logical, because the first function is optimized for (0,0) and the second for (5, 5). Any inbetween solutions
        due to the linear derivative of the 2 objectives is a trade-off.

        R1 - y, R2 - no, R3 - no, R4 - no, R5 - no, R6 - no, R7 - no
        :param x: a list of floats containing the solution's vector of decision variables. Basically, x = Sol.x
        :return: a 2 element tuple, containing the evaluated objectives f1, f2 respectively.
        """
        f1 = x[0]**2 + x[1]**2
        f2 = (x[0] -5 )**2 + (x[1] - 5)**2
        return [f1,f2]


# noinspection PyPep8Naming
class Objectives_2D:
    """
    Class contains objective functions which can be applied to 2-dimensional search spaces.
    """

    # fix
    # should check whether this works for both np arrays and python lists/arrays
    @staticmethod
    def f1(x, A=10):
        return math.pow(x[0] - 5, 2) + math.pow(10*x[1]/A - 6, 2)

    @staticmethod
    def f2(x, A=10):
        return math.pow(x[0] - 7, 2) + math.pow(10*x[1]/A - 6, 2)

