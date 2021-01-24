"""This solves problem #41 of Project Euler (https://projecteuler.net).

Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations

from helpers import chronometric
from mathext import is_prime


@chronometric
def attempt():
    result = 0
    for places in range(2, 10):
        print(places, 'places')
        for pandigital in permutations('123456789'[:places]):
            pandigital = int(''.join(pandigital))
            if is_prime(pandigital):
                print('   ', pandigital)
                result = max(result, pandigital)
    return result


def run_application():

    solution, elapsed = attempt()

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
