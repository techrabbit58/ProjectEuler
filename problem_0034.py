"""This solves problem #34 of Project Euler (https://projecteuler.net).

Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Note: Looking for Wikipedia might be interesting (https://en.wikipedia.org/wiki/Factorion).
"""

from math import factorial


def digit_factorial_sum(n):
    return sum(map(factorial, map(int, list(str(n)))))


def attempt():
    """Once more, finding the upper bound is key."""
    limit = 0
    n = 1
    while factorial(9) * n >= int('9' * n):
        limit = (n + 1) * factorial(9)
        n += 1

    # Now we can look for the solution.
    solution = 0
    for n in range(3, 1 + limit):
        fs = digit_factorial_sum(n)
        if n == fs:
            print(n, digit_factorial_sum(n))
            solution += n
        n += 1

    return solution


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
