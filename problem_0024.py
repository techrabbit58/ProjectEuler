"""This solves problem #24 of Project Euler (https://projecteuler.net).


A permutation is an ordered arrangement of objects. For example, 3124 is one possible
permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or
alphabetically, we call it lexicographic order. The lexicographic permutations of 0,
1 and 2 are:

        012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math


def find_digit_sequence(digits, width, element, limit):
    if len(digits) == 1:
        return str(digits[0])
    step = math.factorial(width - 1)
    d = (limit - element) // step
    element += d * step
    digit = digits[d]
    digits.remove(digit)
    return str(digit) + find_digit_sequence(digits, width - 1, element, limit)


def first_attempt(width=3, limit=4):
    digits = [n for n in range(width)]
    result = find_digit_sequence(digits, width, 0, limit - 1)
    print('Lexically ordered permutation no.', limit)
    print('of digits', digits)
    print('is', result)


def run_application():
    import time
    start = time.time()
    first_attempt(width=10, limit=1_000_000)
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
