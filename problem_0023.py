"""This solves problem #23 of Project Euler (https://projecteuler.net).

A perfect number is a number for which the sum of its proper divisors is exactly equal to the
number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is
called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can
be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be
shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known
that the greatest number that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant
numbers.
"""

from mathext import is_abundant, divisor_sum, sieve, prime_factors


def attempt():
    limit = 28123
    primes = sieve(limit=limit)
    _is_abundant = lambda k: is_abundant(k, divisor_sum(prime_factors(k, iter(primes))))
    abundant = []
    is_sum_of_two = {}
    for n in range(1, limit + 1):
        is_sum_of_two[n] = False
        if _is_abundant(n):
            abundant.append(n)
    for ix, a in enumerate(abundant):
        for b in abundant[ix:]:
            is_sum_of_two[a + b] = True
    result = sum([n for n in is_sum_of_two if not is_sum_of_two[n]])
    print('Solution =', result)


def run_application():
    import time
    start = time.time()
    attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
