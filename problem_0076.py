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

from helpers import chronometric
from mathext import partition

NUMBER = 100


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
