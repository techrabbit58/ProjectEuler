"""This solves problem #48 of Project Euler (https://projecteuler.net).

Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from math import floor, log10


def attempt():
    limit = 1000
    module = 10**10
    result = 1
    for n in range(2, limit + 1):
        result = (result + n**n) % module
    return str(result).rjust(floor(log10(module)), '0')


def run_application():
    import time

    start = time.time()
    solution = attempt()
    elapsed = time.time() - start

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
