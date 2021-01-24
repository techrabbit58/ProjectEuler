"""This solves problem #73 of Project Euler (https://projecteuler.net).

Counting fractions in a range
Problem 73

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5,
5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for
d ≤ 12,000?
"""
from fractions import Fraction

from helpers import chronometric, inclusive_range
from mathext import relative_primes

LOWER_LIMIT = Fraction(1, 3)
UPPER_LIMIT = Fraction(1, 2)
MAX_DENOMINATOR = 12_000


@chronometric
def counting_fractions_in_a_range():
    # TODO: Find the solution. This is not the solution.
    elements = set()
    for denominator in inclusive_range(2, MAX_DENOMINATOR):
        for numerator in relative_primes(denominator):
            fraction = Fraction(numerator, denominator)
            if LOWER_LIMIT < fraction < UPPER_LIMIT:
                print(fraction)
                elements.add(fraction)
    print(len(elements))
    return None


def run_application():
    solution, elapsed = counting_fractions_in_a_range()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code

"""
7295372
"""