"""This solves problem #44 of Project Euler (https://projecteuler.net).

Pentagon numbers
Problem 44

Pentagonal numbers are generated by the formula, P_n=n(3n−1)/2. The first ten pentagonal
numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference, 70 − 22 = 48,
is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k, for which their sum and difference are
pentagonal and D = |P_k − P_j| is minimised; what is the value of D?
"""

from helpers import chronometric
from mathext import pentagonal, is_pentagonal


@chronometric
def attempt():
    j = 0
    found = False
    while not found:
        j += 1
        pj = pentagonal(j)
        for k in range(1, j):
            pk = pentagonal(k)
            d = abs(pj - pk)
            if is_pentagonal(pj + pk) and is_pentagonal(d):
                result = d
                found = True
                break
    return result


def run_application():
    solution, elapsed = attempt()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
