"""This solves problem #46 of Project Euler (https://projecteuler.net).

Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the
sum of a prime and twice a square.

     9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a
square?

I cheated. A quick solution - written in C# - can be found on the web:
https://www.mathblog.dk/project-euler-46-odd-number-prime-square/
That is what I translated to python.
"""

from math import sqrt

from mathext import sieve

PRIMES = [0, 1] + sieve(limit=10000)


def is_twice_a_square(n):
    root = sqrt(n / 2)
    return root == int(root)


def attempt():
    candidate = 1
    is_contradictory = False
    while not is_contradictory:
        candidate += 2
        prime_index = 0
        while candidate >= PRIMES[prime_index]:
            is_contradictory = not is_twice_a_square(candidate - PRIMES[prime_index])
            if not is_contradictory:
                break
            prime_index += 1
    return candidate


def run_application():
    import time

    start = time.time()
    solution = attempt()
    elapsed = time.time() - start

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
