"""This solves problem #6 of Project Euler (https://projecteuler.net)

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the 
square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.
"""

from mathext import gauss_sum, gauss_sum_of_squares


def sum_of_squares(n):
    # formerly by brute force method:
    # return sum(x * x for x in range(1, n + 1))
    return gauss_sum_of_squares(n)


def square_of_sum(n):
    return int(pow(gauss_sum(n), 2))


def run_exercise(*, n=10):
    solution = abs(sum_of_squares(n) - square_of_sum(n))
    print('Solution =', solution)


if __name__ == '__main__':
    run_exercise(n=100)

# last line of code
