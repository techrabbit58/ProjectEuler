"""This solves problem #28 of Project Euler (https://projecteuler.net).
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral
is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def spiral_diagonal_sum(n):
    result = 1
    for k in range(3, n + 1, 2):
        right_upper = k ** 2
        left_upper = right_upper - k + 1
        left_lower = left_upper - k + 1
        right_lower = left_lower - k + 1
        result += right_upper + left_upper + left_lower + right_lower
    return result


def first_attempt():
    print('Solution =', spiral_diagonal_sum(1001))


def run_application():
    import time
    start = time.time()
    first_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
