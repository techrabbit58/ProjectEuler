"""This solves problem #18 of Project Euler (https://projecteuler.net).

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

                3
               7 4
              2 4 6
             8 5 9 3

    (see external file triangle004.txt

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

    (see external file triangle015.txt)

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every
route. However, Problem 67, is the same challenge with a triangle containing one-hundred
rows; it cannot be solved by brute force, and requires a clever method! ;o)

B.t.w. this also solves problem #67, which can not be solved by brute force, but requires
this fancy backwards calculation to be feasible.

    (see external file triangle100.txt)

"""

import time
from collections import deque
from operator import add


def read_triangle(fn):
    stack = deque()
    with open(fn) as fp:
        for line in fp:
            line = [int(n) for n in line.split()]
            if len(line) == 0:
                continue
            stack.append(line)
    return stack


def max_path_sum(triangle):
    if len(triangle) <= 0:
        return 0
    line_a = triangle.pop()
    while len(triangle) > 0:
        line_a = [max(line_a[i], line_a[i + 1]) for i in range(len(line_a) - 1)]
        line_b = triangle.pop()
        line_a = list(map(add, line_a, line_b))
    return line_a[0]


def run_exercise(*, fn='triangle004.txt'):
    triangle = read_triangle(fn)
    result = max_path_sum(triangle)
    print(result)


if __name__ == '__main__':
    print('Running exercise ...')
    start = time.time()
    run_exercise(fn='triangle100.txt')
    print('Runtime =', time.time() - start, 'seconds')
    print('Done.')

# last line of code
