"""This solves problem #233 of Project Euler (https://projecteuler.net).

Lattice points on a circle
Problem 233

Let f(N) be the number of points with integer coordinates that are on a circle passing
through (0,0), (N,0),(0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?
"""
from collections import Counter
from itertools import takewhile

from helpers import chronometric
from mathext import lazy_sieve

START = 359125
STOP = 10 ** 7
CRITERIA = 420

primes = []


def prime_factors(n):
    factors = Counter()
    for k, p in enumerate(primes):
        while n % p == 0:
            factors[p] += 1
            n //= p
        if n == 1:
            break
    return factors


@chronometric
def generate_primes(limit):
    return list(p for p in takewhile(lambda x: x <= limit, lazy_sieve()))


def lattice_points(n):
    h = Counter({p: 2 * e for p, e in prime_factors(n).items()})
    result = 1
    for p, e in h.items():
        if p % 4 == 3 and (e & 1):
            result = 0
            break
        if p % 4 == 1:
            result *= (e + 1)
    result <<= 2
    return result


@chronometric
def lattice_points_on_a_circle():
    # TODO: Find the solution. This is not the solution.
    k = 0
    result = 0
    for n in range(START, STOP + 1):
        if n % 4 == 3:
            continue
        if lattice_points(n) == CRITERIA:
            result += n
            k += 1
            print(k, n, result)
    return None


def lattice_points(n):
    h = Counter({p: 2 * e for p, e in prime_factors(n).items()})
    result = 1
    for p, e in h.items():
        if p % 4 == 3 and (e & 1):
            result = 0
            break
        if p % 4 == 1:
            result *= (e + 1)
    result <<= 2
    return result


def run_application():
    global primes

    print('Generating primes ...')
    primes, elapsed = generate_primes(int(1 + STOP ** 0.5))
    print('Generated {} primes in {} seconds.'.format(len(primes), elapsed))

    print()
    solution, elapsed = lattice_points_on_a_circle()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code

"""
271204031455541309
"""
