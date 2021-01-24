"""This solves problem #387 of Project Euler (https://projecteuler.net).

Harshad Numbers
Problem 387

A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit, always results
in a Harshad number a right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a
strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also
right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is
90619.

You are given that the sum of the strong, right truncatable Harshad primes less than 10^8 is
130459097.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.
"""
from collections import defaultdict
from itertools import takewhile, count

from helpers import chronometric
from mathext import is_prime, digit_sum

EXPONENT = 14
LIMIT = 10 ** (EXPONENT - 1)

harshad_numbers = defaultdict(list)
harshad_numbers[0] += [1, 2, 3, 4, 5, 6, 7, 8, 9]

harshad_strong_right_truncatable_primes = []


def right_truncatable_harshad_numbers():
    for ex in takewhile(lambda x: x <= EXPONENT, count(start=1)):
        for h in harshad_numbers[ex - 1]:
            k = 10 * h
            for d in range(10):
                candidate = k + d
                if not (candidate % digit_sum(candidate)):
                    harshad_numbers[ex].append(candidate)
                    yield candidate


def is_strong(h):
    return is_prime(h / digit_sum(h))


@chronometric
def sum_strong_right_truncatable_harshad_primes():
    result = 0
    for h in takewhile(lambda x: x < LIMIT, right_truncatable_harshad_numbers()):
        if is_strong(h):
            for d in range(1, 10, 2):
                candidate = 10 * h + d
                if is_prime(candidate):
                    result += candidate
    return result


def run_application():
    solution, elapsed = sum_strong_right_truncatable_harshad_primes()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
