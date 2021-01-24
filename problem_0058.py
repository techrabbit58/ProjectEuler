"""This solves problem #58 of Project Euler (https://projecteuler.net).

Spiral primes
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side
length 7 is formed.

                            37 36 35 34 33 32 31
                            38 17 16 15 14 13 30
                            39 18  5  4  3 12 29
                            40 19  6  1  2 11 28
                            41 20  7  8  9 10 27
                            42 21 22 23 24 25 26
                            43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what
is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side
length 9 will be formed. If this process is continued, what is the side length of the square
spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

from helpers import chronometric
from mathext import is_prime


def diagonal_numbers_on_ring(side_length):
    base = pow(side_length, 2)
    delta = side_length - 1
    return {base - delta, base - 2 * delta, base - 3 * delta}


def count_primes(set_of_numbers):
    return len({p for p in set_of_numbers if is_prime(p)})


@chronometric
def attempt():
    limit = 0.1
    side_length = 1
    diagonal_numbers = 1
    diagonal_primes = 0
    while True:
        side_length += 2
        diagonal_numbers += 4
        diagonal_primes += count_primes(diagonal_numbers_on_ring(side_length))
        primes_ratio = diagonal_primes / diagonal_numbers
        if primes_ratio < limit:
            break
    return side_length


def run_application():
    solution, elapsed = attempt()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
