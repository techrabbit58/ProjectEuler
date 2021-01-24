"""This solves problem #97 of Project Euler (https://projecteuler.net).

Large non-Mersenne prime
Problem 97

The first known prime found to exceed one million digits was discovered in 1999, and is a
Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently
other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.
"""

from helpers import chronometric


@chronometric
def attempt():
    return (28433 * pow(2, 7830457, 10**10) % 10**10) + 1


def run_application():
    solution, elapsed = attempt()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
