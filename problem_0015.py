"""This solves problem #15 of Project Euler (https://projecteuler.net).

Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and
down, there are exactly 6 routes to the bottom right corner.

    x ---->
  y 0,0:0--0,1:1--0,2:1
  |    |      |      |
  | 1,0:1--1,1:2--1,2:3
  v    |      |      |
    2,0:1--2,1:3--2,2:6

How many such routes are there through a 20×20 grid?
"""


def paths(n):
    if n < 0:
        raise ValueError('works only for positive integers and zero')
    a = [[0] + n * [1]]
    for y in range(1, n + 1):
        a.append([])
        a[y].append(1)
        for x in range(1, n + 1):
            a[y].append(a[y][x - 1] + a[y - 1][x])
    return a[n][n]


def first_attempt():
    print('Solution =', paths(20))


def run_application():
    import time
    start = time.time()
    first_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
