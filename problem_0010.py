"""This solves problem #10 of Project Euler (https://projecteuler.net).

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time

from mathext import prime_number_generator


def run_exercise(*, limit=10):
    prime = prime_number_generator()
    primes = []
    while True:
        p = next(prime)
        if p >= limit:
            break
        primes.append(p)
    print(sum(primes))


if __name__ == '__main__':
    print('Running exercise ...')
    start = time.time()
    run_exercise(limit=2_000_000)
    print('Runtime =', time.time() - start, 'seconds')
    print('Done.')

# last line of code
