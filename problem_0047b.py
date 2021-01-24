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

This is another attempt, that uses an "inverted" Sieve Of Eratosthenes (find the number of
prime factors of any number in the sieve, and not only if it is prime).
"""
from collections import defaultdict

from helpers import chronometric
from mathext import is_prime


def inverted_sieve(*, limit):
    non_primes = defaultdict(int)
    for factor in range(2, limit + 1):
        if is_prime(factor):
            for n in range(factor * 2, limit + 1, factor):
                non_primes[n] += 1
    return non_primes


def distinct_prime_factors_sequence(*, sequence_length, non_primes):
    candidates = sorted({k for k, v in non_primes.items() if v == sequence_length})
    last_candidate = 0
    sequence = []
    for candidate in candidates:
        if len(sequence) > 0 and candidate - last_candidate > 1:
            sequence = []
        sequence.append(candidate)
        last_candidate = candidate
        if len(sequence) >= sequence_length:
            break
    if len(sequence) != sequence_length:
        sequence = []
    return sequence


@chronometric
def attempt():
    return distinct_prime_factors_sequence(
        sequence_length=4,
        non_primes=inverted_sieve(limit=135000)
    )


def run_application():
    solution, elapsed = attempt()

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
