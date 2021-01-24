"""This solves problem #81 of Project Euler (https://projecteuler.net).

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

    131 673 234 103  18
    201  96 342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524  37 331

Find the minimal path sum, in p081_matrix.txt, a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
"""

import time
from itertools import accumulate
from operator import add


def accumulate_minimum_path(matrix):
    matrix[0] = list(accumulate(matrix[0], add))
    for row in range(1, len(matrix)):
        matrix[row][0] += matrix[row - 1][0]
        for col in range(1, len(matrix[row])):
            matrix[row][col] += min(matrix[row - 1][col], matrix[row][col - 1])
    return matrix


def first_approach():
    matrix = [
        [131, 673, 234, 103,  18],
        [201,  96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524,  37, 331]
    ]
    return matrix


def second_approach():
    matrix = list()
    with open('p081_matrix.txt') as matrix_fp:
        for row in matrix_fp:
            if len(row.strip()) > 0:
                matrix.append([int(n) for n in row.strip().split(',')])
    return matrix


def run_application(func):
    start = time.time()
    print('Solution =', accumulate_minimum_path(func())[-1][-1])
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application(second_approach)

# last line of code
