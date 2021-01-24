"""This solves problem #104 of Project Euler (https://projecteuler.net).

Pandigital Fibonacci ends
Problem 104

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

It turns out that F541, which contains 113 digits, is the first Fibonacci number for which
the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily
in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the
first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine
digits are 1-9 pandigital, find k.

This fast solution is built on a log10 trick, together with the Fibonacci formula of
Moivre/Binet (please see Wikipedia).

See explanations to this fast solution here, which is built on sophisticated math:
https://www.mathblog.dk/project-euler-104-fibonacci-pandigital/
"""
from math import log10

from helpers import chronometric
from mathext import fibonacci_series_m, is_pandigital

sqrt5 = 5 ** 0.5
log_psi = log10((1 + sqrt5) / 2)
log_sqrt5 = log10(sqrt5)
module = 1_000_000_000


@chronometric
def pandigital_fibonacci_ends():
    for k, f in enumerate(fibonacci_series_m(), start=1):
        if is_pandigital(f):
            t = k * log_psi - log_sqrt5
            if is_pandigital(int(pow(10, t - int(t) + 8))):
                break
    return k


def run_application():
    solution, elapsed = pandigital_fibonacci_ends()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
