"""This solves problem #357 of Project Euler (https://projecteuler.net).

Prime generating integers
Problem 357

Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""

from helpers import chronometric

LIMIT = 10 ** 8

PRIMES = {2}


def is_prime(n):
    if n in PRIMES:
        return True
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return False
    PRIMES.add(n)
    return n > 1


def prime_candidates(n):
    for q in range(2, int(n**0.5 + 1)):
        if not n % q:
            yield q + n // q


def is_prime_generating_integer(n):
    for k in prime_candidates(n):
        if not is_prime(k):
            return False
    return True


@chronometric
def prime_generating_integers():
    """
    1) only test numbers p that are prime - 1 (since 1 and p ale always in the set),
       and where p - 1 is divisible by 2, but not by 4 (e.g. 2 + 4k)
    2) instead of divisor list, directly generate the list of remaining candidates
    3) d + n/d is the sum of a divisor plus its complement
    4) do anything as lazy as possible (i.e. generate all lists only as far as you need
    5) stop list generation if you discover the numbers under test not supporting the
       prime generation property
    """
    result = 0
    for n in range(2, 1 + LIMIT, 4):
        if not is_prime(n + 1):
            continue
        if is_prime_generating_integer(n):
            result += n
    return result + 1


def run_application():
    solution, elapsed = prime_generating_integers()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
