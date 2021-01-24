"""This solves problem #357 of Project Euler (https://projecteuler.net).

Prime generating integers
Problem 357

Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""
import itertools

from helpers import chronometric

LIMIT = 10 ** 8

PRIMES = None


def lazy_sieve():
    """This code comes from
    https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188
    which is itself a copy from the Python Cookbook (O'Reilly).
    Very much faster than the former method, checking for primality by subsequent divisions.
    """
    non_primes = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = non_primes.pop(q, None)
        if p is None:
            non_primes[q * q] = q
            yield q
        else:
            x = p + q
            while x in non_primes or not (x & 1):
                x += p
            non_primes[x] = p


@chronometric
def sieve(limit):
    return set(itertools.takewhile(lambda p: p <= limit, lazy_sieve()))


def prime_candidates(n):
    for q in range(2, int(n ** 0.5 + 1)):
        if not n % q:
            yield q + n // q


def is_prime_generating_integer(n):
    for k in prime_candidates(n):
        if k not in PRIMES:
            return False
    return True


@chronometric
def prime_generating_integers(limit):
    """
    1) only test numbers p that are prime - 1 (since 1 and p ale always in the set),
       and where p - 1 is divisible by 2, but not by 4
    2) instead of divisor list, directly generate the list of remaining candidates
    3) d + n/d is the sum of a divisor plus its complement
    4) do anything as lazy as possible (i.e. generate all lists only as far as you need
    5) stop list generation if you discover the numbers under test not supporting the
       prime generation property
    6) do all primality tests by using a pre-generated list of primes
    """
    result = 0
    for n in range(2, 1 + limit, 4):
        if not (n + 1) in PRIMES:
            continue
        if is_prime_generating_integer(n):
            result += n
    return result + 1


def run_application():
    global PRIMES
    print('Preparing primes table ... ', end='')
    PRIMES, elapsed = sieve(LIMIT)
    print('Done in', elapsed)
    print()
    print('Now working on project euler problem no. 357 ... ', end='')
    solution, elapsed = prime_generating_integers(LIMIT)
    print('Done.')
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
