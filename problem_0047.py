"""This solves problem #47 of Project Euler (https://projecteuler.net).

Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

        14 = 2 × 7
        15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

        644 = 2 * 2 ×  7 × 23
        645 =   3   ×  5 × 43
        646 =   2   × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is
the first of these numbers?
"""

from helpers import chronometric
from mathext import prime_factors, sieve


def distinct_prime_factors_sequence(*, sequence_length, primes):
    sequence = []
    n = 3
    last_n = 3
    while True:
        factors = prime_factors(n, iter(primes))
        if len(factors) == sequence_length:
            if n - last_n > 1:
                sequence = []
            sequence.append(n)
            last_n = n
        if len(sequence) == sequence_length:
            break
        n += 1
    return sequence


@chronometric
def attempt():
    print('sieve primes')
    primes = sieve(limit=150000)
    print('primes sieved')
    return distinct_prime_factors_sequence(sequence_length=4, primes=primes)


def run_application():
    solution, elapsed = attempt()

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
