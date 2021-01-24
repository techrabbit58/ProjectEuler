"""This solves problem #56 of Project Euler (https://projecteuler.net).

Powerful digit sum
Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost
unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the
digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

from helpers import chronometric


def digital_sum(n):
    return sum(map(int, str(n)))


@chronometric
def attempt():
    max_digital_sum = 0
    for a in range(95, 100):
        for b in range(95, 100):
            max_digital_sum = max(digital_sum(a**b), max_digital_sum)
    return max_digital_sum


def run_application():
    solution, elapsed = attempt()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
