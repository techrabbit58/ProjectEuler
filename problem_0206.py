"""This solves problem #206 of Project Euler (https://projecteuler.net).

Concealed Square
Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
from math import ceil, floor

from helpers import chronometric


def interleave(n):
    if n < 0 or n > 999999999:
        raise ValueError('Arg must be an integer between 1 and 999999999, or 0.')
    return int('1{}2{}3{}4{}5{}6{}7{}8{}9{}0'.format(*list(str(n).zfill(9))))


def is_template_conforming(n):
    t = int(str(n)[0::2])
    return t == 1234567890


@chronometric
def attempt():
    r = range(1000000000, 1390000000, 10)
    for n in r:
        if n % 100 == 30 or n % 100 == 70:
            if is_template_conforming(n * n):
                solution = n
    return solution


def run_application():
    solution, elapsed = attempt()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
