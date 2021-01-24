"""This solves problem #50 of Project Euler (https://projecteuler.net).

Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

        41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21
terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from helpers import chronometric
from mathext import prime_number_generator, is_prime


@chronometric
def attempt():
    limit = 10 ** 6
    prime = 0
    terms = 1
    prime_sums = [0]
    for p in prime_number_generator():
        prime_sums.append(prime_sums[-1] + p)
        if prime_sums[-1] >= limit:
            break
    candidates = []
    for j in range(len(prime_sums)):
        for k in range(j):
            candidate = prime_sums[j] - prime_sums[k]
            if is_prime(candidate):
                candidates.append((candidate, j - k))
                break
    return max(candidates, key=lambda x: x[terms])[prime]


def run_application():
    solution, elapsed = attempt()

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
