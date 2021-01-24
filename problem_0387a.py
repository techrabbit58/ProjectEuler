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
from itertools import takewhile

from helpers import chronometric
from mathext import lazy_sieve

EXPONENT = 4
LIMIT = 10 ** EXPONENT

primes = set()


def is_right_truncatable_harshad_number(n, digits):
    if len(digits) > 1:
        return not n % sum(digits) and is_right_truncatable_harshad_number(n // 10, digits[:-1])
    return n > 0


def is_strong_right_truncatable_harshad_number(n):
    if not n:
        return False
    digits = [int(d) for d in str(n)]
    k, r = divmod(n, sum(digits))
    if r:
        return False
    if k not in primes:
        return False
    if not is_right_truncatable_harshad_number(n // 10, digits[:-1]):
        return False
    return True


@chronometric
def primes_first():
    # This solution is still too slow.
    result = 0
    for p in takewhile(lambda x: x < LIMIT, lazy_sieve()):
        primes.add(p)
        if p < 10:
            continue
        if is_strong_right_truncatable_harshad_number(p // 10):
            result += p
    return result


def run_application():
    solution, elapsed = primes_first()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
