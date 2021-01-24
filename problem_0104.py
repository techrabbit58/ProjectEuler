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
"""

from helpers import chronometric
from mathext import fibonacci_series, is_pandigital

sqrt5 = 5 ** 0.5
inverse_sqrt5 = 1 / sqrt5
psi = (1 + sqrt5) / 2


@chronometric
def pandigital_fibonacci_ends():
    for k, f in enumerate(fibonacci_series(), start=1):
        if is_pandigital(str(f % 1000000000)):
            s = str(f)
            print(k)
            if is_pandigital(s[:9]):
                result = k
                break
    return result


def run_application():
    solution, elapsed = pandigital_fibonacci_ends()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
