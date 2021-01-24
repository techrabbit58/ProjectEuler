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
from collections import Counter
from functools import lru_cache, reduce
from itertools import takewhile

from helpers import chronometric
from mathext import lazy_sieve, mod_inv

MODULE = 10 ** 9 + 7
LIMIT = 20000
primes = None
factorizations = None
factorized_powers = None


@lru_cache(maxsize=None)
def prime_factors(n):
    prime = primes.__iter__()
    factors = Counter()
    p = next(prime)
    while n > 1:
        if n % p == 0:
            factors[p] += 1
            n //= p
        else:
            p = next(prime)
    return factors


@lru_cache(maxsize=None)
def factorized_factorial(n):
    if n < 2:
        return Counter()
    return factorized_factorial(n - 1) + factorizations[n]


def factorized_to_the_power_of_self(n):
    if n < 2:
        return Counter()
    return factorized_powers[n]


@lru_cache(maxsize=None)
def B(n):
    if n < 2:
        return Counter()
    return B(n - 1) + factorized_to_the_power_of_self(n) - factorized_factorial(n)


def D(factorization):
    if not factorization:
        return 1
    return reduce(lambda a, b: (a * b) % MODULE, [
        (pow(n, x + 1, MODULE) - 1) * mod_inv(n - 1, MODULE)
        for n, x in factorization.items()
    ])


def S(n):
    result = 0
    for m in range(1, 1 + n):
        result = (result + D(B(m))) % MODULE
    return result


@chronometric
def generate_primes(limit):
    return tuple(p for p in takewhile(lambda x: x <= limit, lazy_sieve()))


@chronometric
def generate_prime_factors(limit):
    return {n: prime_factors(n) for n in range(2, 1 + limit)}


@chronometric
def generate_factorized_powers(factorizations_):
    return {n: Counter({k: v * n for k, v in f.items()}) for n, f in factorizations_.items()}


@chronometric
def divisors_of_binomial_product(n):
    print('Calculate S({}) ...'.format(n))
    result = S(n)
    print('Done.')
    return result


def run_application():
    global primes
    global factorizations
    global factorized_powers

    print('Generating primes ...')
    primes, elapsed = generate_primes(LIMIT)
    print('Generated {} primes in {} seconds.'.format(len(primes), elapsed))

    print('Find prime factors ...')
    factorizations, elapsed = generate_prime_factors(LIMIT)
    print('Done finding prime factors in {} seconds.'.format(elapsed))

    print('Calculate powers ...')
    factorized_powers, elapsed = generate_factorized_powers(factorizations)
    print('Done calculating powers in {} seconds.'.format(elapsed))

    print()
    solution, elapsed = divisors_of_binomial_product(LIMIT)
    print()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code

"""
Generating primes ...
Generated 2262 primes in 0.024099800000000005 seconds.
Find prime factors ...
Done finding prime factors in 2.0088691 seconds.
Calculate powers ...
Done calculating powers in 0.3900591000000002 seconds.

Calculate S(20000) ...
Done.

Solution = 538319652
Runtime = 303.1360464 seconds

Process finished with exit code 0
"""
