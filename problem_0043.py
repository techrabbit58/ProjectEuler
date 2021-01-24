"""This solves problem #43 of Project Euler (https://projecteuler.net).

Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the
digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility
property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4  = 406 is divisible by 2
    d3d4d5  = 063 is divisible by 3
    d4d5d6  = 635 is divisible by 5
    d5d6d7  = 357 is divisible by 7
    d6d7d8  = 572 is divisible by 11
    d7d8d9  = 728 is divisible by 13
    d8d9d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations

from helpers import chronometric


@chronometric
def attempt():
    pandigitals = set()
    substring_primes = (2, 3, 5, 7, 11, 13, 17)
    d2, d8 = 1, 7
    for pandigital in permutations('0123456789'):
        chunks = (int(''.join(pandigital[k:k+3])) for k in range(d2, d8 + 1))
        if all(a % b == 0 for a, b in zip(chunks, substring_primes)):
            pandigitals.add(int(''.join(pandigital)))
    return sum(pandigitals)


def run_application():

    solution, elapsed = attempt()

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
