"""This solves problem #32 of Project Euler (https://projecteuler.net).

Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as
a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once
in your sum.
"""

from itertools import permutations


def first_attempt():
    products = set()
    for p in permutations('123456789'):
        for a in range(1, len(p)):
            for b in range(a + 1, len(p)):
                multiplicand = int(''.join(p[:a]))
                multiplier = int(''.join(p[a:b]))
                product = int(''.join(p[b:]))
                if multiplicand * multiplier == product:
                    products.add(product)
    print('Solution =', sum(products))


def run_application():
    import time
    start = time.time()
    first_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
