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
START = 10 ** 7
STOP = 2 * 10 ** 7
HALF = STOP // 2
CRITERIA = 420

primes = None


def prime_factors(n):
    factors = Counter()
    for p in primes:
        while n % p == 0:
            factors[p] += 1
            n //= p
        if n == 1:
            break
    return factors


@chronometric
def generate_primes(limit):
    return tuple(p for p in takewhile(lambda x: x <= limit, lazy_sieve()))


def perimeter_lattice_points(n):
    """Calculate the perimeter lattice points for a given N.

    We interpret N as the radius of a circle, centered at (0, 0).

    For details, please see http://oeis.org/A046109
    and/or http://mathworld.wolfram.com/SumofSquaresFunction.html
    """
    if n % 4 == 3:
        return 4
    result = 1
    for p, e in prime_factors(n).items():
        if p % 4 == 1:
            result *= (e << 1) + 1
    return result << 2


@chronometric
def lattice_points_on_a_circle():
    """
    This approach tries to make things easier by transposing the circle from
    mid point (n/2, n/2) to (0, 0) and N from being cut to N being radius. The
    goal is to have easier numbers (more integers), and to do less calculations.
    The solution makes use of the formula found at:
    http://mathworld.wolfram.com/CircleLatticePoints.html
    """
    # TODO: Find the solution. This is not the solution.
    k = 0
    good_circles = set()
    for n in range(START, STOP + 1):
        if n in good_circles:
            k += 1
            print(k, n, '*')
            continue
        if perimeter_lattice_points(n) == CRITERIA:
            good_circles.add(n)
            if n <= HALF:
                good_circles.add(n << 1)
            k += 1
            print(k, n)
    print(sum(good_circles))
    return None


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
