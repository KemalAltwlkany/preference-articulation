import math as math


class Objectives:
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

