import math as math


class MOO_Problem:
    """
    Class is never to be instantiated in the first place, its just a wrapper to keep all the benchmark functions used
    in one nice class, which should be used as static functions.
    """

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
        :return: a 2 element list, containing the evaluated objectives; f1, f2 respectively.
        """
        f1 = x[0]**2 + x[1]**2
        f2 = (x[0] -5)**2 + (x[1] - 5)**2
        return [f1, f2]

    @staticmethod
    def IM1(x):
        """
        The IM1 Test problem.
        In the work of S. Huband, this test problem is labeled "IM1"
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

        Pareto optimal front is obtain for x2=2.
        Cited from:
        M. Tadahiko, H. Ishibuchi - MOGA: Multi-Objective Genetic Algorithms
        :param x: a list of floats containing the solution's vector of decision variables. Basically, x = Sol.x
        :return: a 2 element list, containing the evaluated objectives; f1, f2 respectively.
        """
        f1 = 2*math.sqrt(x[0])
        f2 = x[0]*(1-x[1]) + 5
        return [f1, f2]


