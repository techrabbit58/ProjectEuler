"""This solves problem #4 of Project Euler (https://projecteuler.net)

A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time

from mathext import is_palindrome


def run_experiment():
    """Run the palindrome experiment."""
    palindromes = set()
    for i in range(100, 1000):
        for j in range(i, 1000):
            candidate = i * j
            if is_palindrome(candidate):
                palindromes.add(candidate)
    print('max of palindromes =', max(palindromes))


if __name__ == '__main__':
    start = time.time()
    run_experiment()
    print('runtime =', time.time() - start, 'seconds')

# last line of code
