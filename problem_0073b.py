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

from helpers import chronometric

LOWER_LIMIT = Fraction(1, 3)
UPPER_LIMIT = Fraction(1, 2)
MAX_DENOMINATOR = 12_000

"""
This implementation uses a recursive approach, in that it counts all fractions between
lower and upper boundaries. Since we are not interested in the fraction values, we do not
care the numerators, and do only count the denominators (in a pars pro toto style).

To bypass the ever growing stack problem, the recursion has been serialized by using a stack.

The algorithm is based on the mediant function, which says, that between two fractions,
there is always a mediant fraction with the sum of both numerators divided by the sum of both
denominators. We use this function recursively between any two fractions we subsequently get.

This solution is from the problem solution documentation provided by Project Euler.
"""


@chronometric
def counting_fractions_in_a_range():
    limit = MAX_DENOMINATOR
    count = 0
    stack = []
    left = LOWER_LIMIT.denominator
    right = UPPER_LIMIT.denominator
    while True:
        mediant = left + right
        if mediant > limit:
            if len(stack) > 0:
                left = right
                right = stack.pop()
            else:
                break
        else:
            count += 1
            stack.append(right)
            right = mediant
    return count


def run_application():
    solution, elapsed = counting_fractions_in_a_range()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code

"""
Solution = 7295372
Runtime = 7.9537178 seconds
"""
