"""This solves problem #53 of Project Euler (https://projecteuler.net).

Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

Let us use the notation, 5C3=10.

In general, nCr = n! * r! / (n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: 23C10=1144066.

How many, not necessarily distinct, values of nCr for 1≤n≤100, are greater than one-million?
"""

from helpers import chronometric
from mathext import binomial


@chronometric
def attempt():
    solution = 0
    for n in range(1, 1 + 100):
        for r in range(1, 1 + n):
            x = binomial(n, r)
            if x > 1000000:
                solution += 1
    return solution


def run_application():
    solution, elapsed = attempt()

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
