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
from functools import lru_cache
from itertools import takewhile
from math import factorial

from helpers import chronometric
from mathext import lazy_sieve, prime_factors

MODULE = 10 ** 9 + 7
primes = None


@lru_cache(maxsize=None)
def binomial_product(n):
    if n == 1:
        return 1
    return binomial_product(n - 1) * n ** n // factorial(n)


def geometric_sum(p, k):
    return ((p ** (k + 1) - 1) // (p - 1)) % MODULE


def divisor_sum(n):
    pf = prime_factors(n, primes.__iter__())
    sum_ = 1
    for p, k in pf.items():
        sum_ = (sum_ * geometric_sum(p, k)) % MODULE
    return sum_


def sum_of_divisor_sums(n):
    sum_ = 0
    for ds in [divisor_sum(binomial_product(k)) for k in range(1, 1 + n)]:
        sum_ = (sum_ + ds) % MODULE
    return sum_


@chronometric
def divisors_of_binomial_product():
    # TODO: Find the solution. This is not the solution.
    # print(binomial_product(5))
    # print(sum_of_divisor_sums(5))
    # print(binomial_product(10))
    # print(sum_of_divisor_sums(10))
    # print(binomial_product(100))
    print(sum_of_divisor_sums(100))
    # print(binomial_product(20000))
    # print(sum_of_divisor_sums(20000))
    return None


@chronometric
def generate_primes(limit):
    return [p for p in takewhile(lambda x: x <= limit, lazy_sieve())]


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
