"""This solves problem #76 of Project Euler (https://projecteuler.net).

Counting summations
Problem 76

It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
from functools import lru_cache
from math import floor

from helpers import chronometric

NUMBER = 100


@lru_cache(maxsize=None)
def _partition(n, k):
    if k > n or n == 0:
        return 0
    elif k == 1 or k == n:
        return 1
    elif k == 2:
        return floor(n / 2)
    elif k == 3:
        return round(n * n / 12)
    else:
        return _partition(n - 1, k - 1) + _partition(n - k, k)


def partition(n):
    return sum(_partition(n, i) for i in range(1, n + 1))


@chronometric
def counting_summations(number):
    return partition(number) - 1


def run_application():
    solution, elapsed = counting_summations(NUMBER)
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
