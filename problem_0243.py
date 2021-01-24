"""This solves problem #243 of Project Euler (https://projecteuler.net).

A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its
proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""

from fractions import Fraction

from mathext import euler_phi, prime_number_generator


def denominator_resilience(d):
    return Fraction(euler_phi(d), d - 1)


def attempt():
    """Builds a product from consecutive ascending primes until we not longer exceed the limit.
    Then goes back by dividing the denominator so far by the last prime, and then stepping up
    by multiplying by two (i.e. growing the denominator the smallest possible step) for
    several rounds.
    CAVEAT! To be sure really having found the smallest denominator, some testing and
    optimizing is necessary. There might still be smaller denominators in the wild.
    """
    limit = Fraction(15499, 94744)
    # limit = Fraction(4, 10)
    prime = prime_number_generator()
    denominator = next(prime)
    while denominator_resilience(denominator) >= limit:
        p = next(prime)
        denominator *= p
    denominator //= p
    # prime = prime_number_generator()
    while denominator_resilience(denominator) >= limit:
        # denominator *= next(prime)
        denominator *= 2
    print('R({}) = {} and is less than {}.'.format(
        denominator, denominator_resilience(denominator), limit))


def run_application():
    import time
    start = time.time()
    attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
