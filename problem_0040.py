"""This solves problem #40 of Project Euler (https://projecteuler.net).

=== Champernowne's constant ===

An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following
expression.

    d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

from functools import reduce
from operator import mul


def first_attempt():
    champernowne_constant = ''.join([str(n) for n in range(185_186)])
    digits_of_solution = (1, 10, 100, 1_000, 10_000, 100_000, 1_000_000)
    solution = reduce(mul, (int(champernowne_constant[d]) for d in digits_of_solution))
    return solution


def run_application():
    import time

    start = time.time()
    solution = first_attempt()
    runtime = time.time() - start

    print('Solution:', solution)
    print('Runtime =', runtime, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
