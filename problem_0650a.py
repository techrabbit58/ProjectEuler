"""This solves problem #650 of Project Euler (https://projecteuler.net).

Divisors of Binomial Product
Problem 650

Let B(n)=product(k=0, to=n, nCr(n, k)), a product of binomial coefficients.

For example, B(5)=nCr(5,0)×nCr(5,1)×nCr(5,2)×nCr(5,3)×nCr(5,4)×nCr(5,5)=1×5×10×10×5×1=2500.

Let D(n)=sum(d|B(n), d), the sum of the divisors of B(n).

For example, the divisors of B(5) are 1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500, 625,
1250 and 2500,

so D(5) = 1 + 2 + 4 + 5 + 10 + 20 + 25 + 50 + 100 + 125 + 250 + 500 + 625 + 1250 + 2500 = 5467.

Let S(n)=sum(k=1, to=n, D(k)).

You are given S(5)=5736, S(10)=141740594713218418 and S(100) mod 1000000007=332792866.

Find S(20000) mod 1000000007.
"""
from collections import Counter, deque, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import takewhile

from helpers import chronometric
from mathext import lazy_sieve

MODULE = 10 ** 9 + 7
primes = None


@lru_cache(maxsize=None)
def prime_factors(n):
    prime = primes.__iter__()
    factors = defaultdict(int)
    p = next(prime)
    while n > 1:
        if n % p == 0:
            factors[p] += 1
            n //= p
        else:
            p = next(prime)
    return factors


@lru_cache(maxsize=None)
def geometric_sum(p, k):
    return int(Fraction(pow(p, (k + 1)) - 1, p - 1)) % MODULE


def binomial_product_divisor_sums():
    n = 1
    yield n, 1
    current_row = [1, 1]
    while True:
        n += 1
        new_row = [1]
        pf = Counter()
        for k in range(0, n - 1):
            coefficient = current_row[k] + current_row[k + 1]
            new_row.append(coefficient)
            pf.update(prime_factors(coefficient))
        current_row = new_row + [1]
        result = 1
        for p, k in pf.items():
            result = (result * geometric_sum(p, k)) % MODULE
        yield n, result


def sum_of_divisor_sums(n):
    sum_ = 0
    for k, ds in takewhile(lambda x: x[0] <= n, binomial_product_divisor_sums()):
        if not k % 10:
            print('.', end='' if k % 500 else '\n')
        sum_ = (sum_ + ds) % MODULE
    print()
    return sum_


@chronometric
def divisors_of_binomial_product():
    # TODO: Find the solution. This is not the solution.
    # print(sum_of_divisor_sums(5))
    print(sum_of_divisor_sums(100))
    # print(sum_of_divisor_sums(20000))
    return None


@chronometric
def generate_primes(limit):
    return tuple(p for p in takewhile(lambda x: x <= limit, lazy_sieve()))


def run_application():
    global primes

    print('Generating primes ...')
    primes, elapsed = generate_primes(10 ** 5)
    print('Generated {} primes in {} seconds.'.format(len(primes), elapsed))

    solution, elapsed = divisors_of_binomial_product()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
