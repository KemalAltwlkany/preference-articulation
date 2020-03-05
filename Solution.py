# The solution class is a simple wrapper that contains information about the solution in the SearchSpace, that is the
# vector of parameters (x), and the vector of evaluated objective functions (y) for that solution.


class Solution:
    def __init__(self, x):
        self.x = x
        self.y = []

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

