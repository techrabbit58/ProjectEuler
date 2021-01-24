"""This solves problem #52 of Project Euler (https://projecteuler.net).

Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same
digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same
digits.
"""
from functools import partial
from itertools import count

from helpers import chronometric


def is_anagram_equivalence(s, t):
    return sorted(list(str(s))) == sorted(list(str(t)))


@chronometric
def attempt():
    for x in count(100000):
        compare = partial(is_anagram_equivalence, x)
        if all(map(compare, (n * x for n in (2, 3, 4, 5, 6)))):
            solution = x
            break
    return solution


def run_application():
    solution, elapsed = attempt()

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
