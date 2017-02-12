"""simplex method solver"""

import argparse
import numpy as np
from scipy.optimize import linprog


class Simplex:

    def __init__(self, c, A, b, min_or_max):
        self.c = c
        self.A = A
        self.b = b
        self.min_or_max = min_or_max

    def solver(self):
        if self.min_or_max == 'max':
            self.c *= -1.0

        bnds_xs = [(0, None) for i in self.c]
        bounds = ()

        for i in bnds_xs:
            bounds += ((i,))

        sol = linprog(self.c, A_ub=self.A, b_ub=self.b, bounds=bounds, options={"disp" : True})

        print sol


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--c", nargs='+', type=int, help="objective function coefficients", required=True)
    argparser.add_argument("--A", nargs='+', type=list, help="constraints", required=True)
    argparser.add_argument("--b", nargs='+', type=int, help="b vector", required=True)
    argparser.add_argument("--opt_type", type=str, help="max or min function", required=True)

    args = argparser.parse_args()

    matrix_A = []
    sub_arr = []
    
    for i in args.A:
        for j in i:
            sub_arr.append(int(j))

        matrix_A.append(sub_arr)
        sub_arr = []

    args.c = np.array(args.c, dtype=np.float64)
    args.A = np.array(matrix_A, dtype=np.float64)
    args.b = np.array(args.b, dtype=np.float64)

    n = Simplex(args.c, args.A, args.b, args.opt_type)
    n.solver()
