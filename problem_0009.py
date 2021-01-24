"""This solves problem #9 of Project Euler (https://projecteuler.net).

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time
from functools import reduce
from operator import mul


def run_exercise():
    triples = []
    s = 1000
    for a in range(3, 1 + (s - 3) // 3):
        for b in range(a + 1, 1 + (s - 1 - a) // 2):
            c = s - a - b
            if a * a + b * b == c * c:
                triples.append((a, b, c))
    print('Found triples:')
    print(triples)
    print('The product of the first triple is:', reduce(mul, triples[0]))


if __name__ == '__main__':
    print('Running exercise ...')
    start = time.time()
    run_exercise()
    print('Runtime =', time.time() - start, 'seconds')
    print('Done.')

# last line of code
