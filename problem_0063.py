"""This solves problem #63 of Project Euler (https://projecteuler.net).

Powerful digit counts
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number,
134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

                               - - -  * * *  - - -
S O L U T I O N

Find the number of positive integers x that have the property 10^(n-1) <= x^n < 10^n.

The upper bound for each order of magnitude is 9, since x must be an integer.
The lower bound is 10^((n-1)/n). Again, x must be an integer, and n is the order of magnitude.
So x might vary, in any order of magnitude, between and inclusive lower bound and upper bound.

We stop counting per order of magnitude, as soon as the lower bound becomes greater than the
upper bound, which is 9.
"""
import math

from helpers import chronometric


@chronometric
def attempt():
    powerful_digit_counts = 0
    magnitude = 1
    upper_bound = 9
    while True:
        lower_bound = math.ceil(pow(10, (magnitude - 1) / magnitude))
        if lower_bound > upper_bound:
            break
        powerful_digit_counts += upper_bound + 1 - lower_bound
        print(powerful_digit_counts, upper_bound + 1 - lower_bound, magnitude)
        magnitude += 1
    return powerful_digit_counts


def run_application():
    solution, elapsed = attempt()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
