"""This solves problem #72 of Project Euler (https://projecteuler.net).

Counting fractions
Problem 72

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5,
5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

from helpers import chronometric, inclusive_range
from mathext import euler_phi

LIMIT = 1_000_000


@chronometric
def counting_fractions():
    return sum(euler_phi(denominator) for denominator in inclusive_range(2, LIMIT))


def run_application():
    solution, elapsed = counting_fractions()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code

"""
Solution = 303963552391
Runtime = 58.571103799999996 seconds
"""
