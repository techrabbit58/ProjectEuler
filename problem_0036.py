"""This solves problem #36 of Project Euler (https://projecteuler.net).

Double-base palindromes

The decimal number, 585 (decimal) = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from mathext import palindromes, is_bitwise_palindrome


def attempt():
    solution = 0
    for palindrome in palindromes():
        if not palindrome < 1_000_000:
            break
        if is_bitwise_palindrome(palindrome):
            solution += palindrome
    return solution


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
