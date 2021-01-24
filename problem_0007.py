"""This solves problem #7 of Project Euler (https://projecteuler.net)

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime
is 13.

What is the 10001st prime number?

"""

import time

from mathext import prime_number_generator


def run_exercise(*, n=6):
    primes = []
    for p in prime_number_generator():
        primes.append(p)
        n -= 1
        if not n > 0:
            break
    print('Solution =', primes[-1])


if __name__ == '__main__':
    start = time.time()
    run_exercise(n=10001)
    print('Runtime =', time.time() - start, 'seconds')

# last line of code
