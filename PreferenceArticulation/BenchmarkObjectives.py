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



print(Objectives.quadratic([2, 10]))