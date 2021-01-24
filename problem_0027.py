"""This solves problem #27 of Project Euler (https://projecteuler.net).

Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values
0≤n≤39. However, when n = 40, 40^2 + 40 + 41 = 40 (40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the
consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n=0.
"""

import time

from mathext import is_prime


def euler_polynomial(a, b, x):
    return x * x + a * x + b


def first_approach():
    coefficients = []
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            if not is_prime(euler_polynomial(a, b, 0)):
                continue
            else:
                x = 1
                while is_prime(euler_polynomial(a, b, x)):
                    x += 1
                coefficients.append((a, b, x))
    a, b, _ = max(coefficients, key=lambda k: k[2])
    print('Solution =', a * b)


def run_application():
    start = time.time()
    first_approach()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
