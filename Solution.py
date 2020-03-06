# The solution class is a simple wrapper that contains information about the solution in the SearchSpace, that is the
# vector of parameters (x), and the vector of evaluated objective functions (y) for that solution.
import math as math


class Solution:
    eps = 0.000001

    def __init__(self, x):
        self.x = x
        self.y = []

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # Two solution instances are equal if their x-vector is roughly the same. There is logically
    # no need for checking the y vector as well. "Roughly the same" is defined by class static
    # attribute Solution.eps which defines the relative and absolute tolerance allowed between
    # individual coordinates.
    def __eq__(self, other):
        if isinstance(other, Solution):
            for i,j in zip(self.x, other.x):
                if math.isclose(i, j, rel_tol=Solution.eps, abs_tol=Solution.eps):
                    continue
                else:
                    return False
        return True

