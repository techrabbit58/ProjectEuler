"""This solves problem #99 of Project Euler (https://projecteuler.net).

Largest exponential
Problem 99

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult,
as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult,
as both numbers contain over three million digits.

Using 'p099_base_exp.txt', a 22K text file containing one thousand lines with a base/exponent
pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
from math import log2
from collections import namedtuple

from helpers import chronometric

ExponentialNumber = namedtuple('ExponentialNumber', 'base exponent')


@chronometric
def largest_exponential(file='p099_base_exp.txt'):
    largest = ExponentialNumber(1, 0)
    line_of_largest = 0
    with open(file) as fp:
        for k, line in enumerate(fp, start=1):
            x = ExponentialNumber(*[int(s) for s in line.strip().split(',')])
            if log2(x.base) * x.exponent > log2(largest.base) * largest.exponent:
                largest = x
                line_of_largest = k
    return line_of_largest


def run_application():
    solution, elapsed = largest_exponential()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
