"""This solves problem #78 of Project Euler (https://projecteuler.net).

Let p(n) represent the number of different ways in which n coins can be separated into piles.
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

    OOOOO
    OOOO O
    OOO OO
    OOO O O
    OO OO O
    OO O O O
    O O O O O

Find the least value of n for which p(n) is divisible by one million.
"""

from functools import lru_cache
from math import floor

from mathext import pentagonal


@lru_cache(maxsize=None)
def _partition(n, k):
    if k > n or n == 0:
        return 0
    elif k == 1 or k == n:
        return 1
    elif k == 2:
        return floor(n / 2)
    elif k == 3:
        return round(n * n / 12)
    else:
        return _partition(n - 1, k - 1) + _partition(n - k, k)


def partition(n):
    return sum(_partition(n, i) for i in range(1, n + 1))


def first_attempt():
    n = 1
    while True:
        p = partition(n) % 1_000_000
        print(n, p)
        if p == 0:
            break
        n += 1
    return n


def second_attempt():

    k = sum([[pentagonal(i), pentagonal(-i)] for i in range(1, 250)], [])

    p, sign, n, mod = [1], [1, 1, -1, -1], 0, 1_000_000

    while p[n] > 0:
        n += 1
        px, i = 0, 0
        while k[i] <= n:
            px += p[n - k[i]] * sign[i % 4]
            i += 1
        p.append(px % mod)

    return n


def run_application():
    import time
    start = time.time()
    n = second_attempt()
    print('The least value of n for which p(n) is divisible by 1.000.000 is')
    print()
    print('     ', n)
    print()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
