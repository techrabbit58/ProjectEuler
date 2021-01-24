"""A little extension to the python3 math library.

B.t.w. when called as a standalone script, it solves Problem #5 of Project Euler
(https://projecteuler.net): 2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder. What is the smallest positive
number that is evenly divisible by all of the numbers from 1 to 20?
"""

import itertools
from collections import defaultdict
from fractions import Fraction
from functools import reduce, lru_cache
from math import gcd, sqrt, log10
from operator import mul
from typing import Set

hcf = gcd


@lru_cache(maxsize=None)
def binomial(n, k):
    try:
        if (k << 1) > n:
            return binomial(n, n - k)
        if k == 0:
            return 1
        if k == 1:
            return n
        return binomial(n - 1, k - 1) + binomial(n - 1, k)
    except ValueError:
        pass
    return 0


def hyperfactorial(n):
    return reduce(mul, [pow(k, k) for k in range(1, 1 + n)])


def superfactorial(n):
    return reduce(mul, [pow(k, n - k + 1) for k in range(1, 1 + n)])


def binomial_product(n):
    return hyperfactorial(n) // superfactorial(n)


def is_odd(n: int) -> bool:
    return abs(n) & 0x1 == 1


def is_even(n: int) -> bool:
    return abs(n) & 0x1 == 0


def num_digits(n):
    return int(log10(n)) + 1


def digit_sum(n):
    """Calculating with integer arithmetic instead of char/int/list method
    doubles the speed.
    """
    result = 0
    while n:
        result += n % 10
        n = n // 10
    return result


def gauss_sum(n):
    """Calculate sum(x for x in range(1, n+1)) by formula."""
    return n * (n + 1) // 2


def gauss_sum_of_squares(n):
    """Calculate sum(x * x for x in range(1, n+1)) by formula."""
    return (2 * n + 1) * (n + 1) * n // 6


def lcm(m, n):
    return m * n // gcd(m, n)


def reversed_euklid(chain_fraction):
    from fractions import Fraction
    r, b = 0, 1
    for q in reversed(chain_fraction):
        a = b * q + r
        b, r = a, b
    return Fraction(b, r)


def extended_gcd(aa, bb):
    last_remainder, remainder = abs(aa), abs(bb)
    x, last_x, y, last_y = 0, 1, 1, 0
    while remainder:
        last_remainder, (quotient, remainder) = remainder, divmod(last_remainder, remainder)
        x, last_x = last_x - quotient * x, x
        y, last_y = last_y - quotient * y, y
    return last_remainder, last_x * (-1 if aa < 0 else 1), last_y * (-1 if bb < 0 else 1)


@lru_cache(maxsize=None)
def mod_inv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def star_lcm(a_list_of_numbers):
    return reduce(lcm, a_list_of_numbers)


def sieve(*, limit):
    return set(itertools.takewhile(lambda p: p < limit, lazy_sieve()))


def prime_factors(n, primes):
    """Find all prime factors of n.
    :parameter n: is the number to find the factors for
    :parameter primes: is an iterable providing enough prime numbers to do the trick
    :returns: a dictionary with prime factors = key and exponents of prime factors as values
    """
    factors = defaultdict(int)
    for p in primes:
        while n % p == 0:
            factors[p] += 1
            n //= p
        if n == 1:
            break
    return dict(factors)


def mediant(a: Fraction, b: Fraction) -> Fraction:
    return Fraction(a.numerator + b.numerator, a.denominator + b.denominator)


def divisors(n: int) -> Set[int]:
    """n must be a positive integer."""
    result = set((1, n))
    limit = int(n ** 0.5) + 1
    for q in range(2, limit):
        k, r = divmod(n, q)
        if not r:
            result.update((k, q))
    return result


def sigma(n):
    """Calculate the sum of all divisors of N."""
    return sum(divisors(n))


def sigma_star(n):
    """Calculate the sum of all *proper* divisors of N."""
    return sum(divisors(n)) - n


def divisor_count(factors):
    num_divisors = 1
    for a in factors.values():
        num_divisors *= a + 1
    return num_divisors


def divisor_sum(factors):
    result = 1
    for p, a in factors.items():
        result *= (p ** (a + 1) - 1) // (p - 1)
    return result


def is_deficient(n, div_sum):
    return (2 * n) > div_sum


def is_abundant(n, div_sum):
    return (2 * n) < div_sum


def is_perfect(n, div_sum):
    return (2 * n) == div_sum


def is_prime(n):
    """Rabin-Miller test for primality.
    Code borrowed from a forum post about #387 of user 'oskros'.
    This is **really** fast!"""
    if n < 2:
        return False
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    if n in witnesses:
        return True
    if n % 6 not in [1, 5]:
        return False
    r, s = 1, n - 1
    while s % 2 == 0:
        s //= 2
        r += 1
    for witness in witnesses:
        remainder = pow(witness, s, n)
        if remainder == 1:
            continue
        for pow_of_2 in range(1, r):
            if remainder == n - 1:
                break
            remainder = pow(remainder, 2, n)
        else:
            return False
    return True


def relative_primes(module):
    """Find all relative primes in module *module*. Return a set of all values that match."""
    if module == 1:
        return set()
    candidates = set(range(1, module))
    if is_prime(module):
        return candidates
    candidate = 2
    while True:
        if not module % candidate:
            k = candidate
            while k < module:
                candidates -= {k}
                k += candidate
        if candidate ** 2 > module:
            break
        candidate += 1
        while candidate not in candidates:
            candidate += 1
    return candidates


def euler_phi(n):
    """Count all factors of n that give gcd(factor, n) == 1. This implementation follows the
    example and explanation at https://www.geeksforgeeks.org/eulers-totient-function/
    and uses another formula of L. Euler, the 'product formula', instead of the gcd().
    But the basic idea is still phi = len(find_relative_primes(n)).
    """
    if is_prime(n):
        return n - 1
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def prime_number_generator():
    yield from lazy_sieve()


def lazy_sieve():
    """This code comes from
    https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188
    Very much faster than the former method, checking for primality by subsequent divisions.
    """
    non_primes = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = non_primes.pop(q, None)
        if p is None:
            non_primes[q * q] = q
            yield q
        else:
            x = p + q
            while x in non_primes or not (x & 1):
                x += p
            non_primes[x] = p


def primes_with_one():
    yield 1
    yield from lazy_sieve()


def palindromes():
    for palindrome in range(1, 10):
        yield palindrome

    current_places = 2
    while True:
        current_prefix = current_places // 2
        has_middle_digit = current_places % 2 == 1
        for n in range(10 ** (current_prefix - 1), 10 ** current_prefix):
            first = str(n)
            last = first[::-1]
            if has_middle_digit:
                for middle in '0123456789':
                    palindrome = int(first + middle + last)
                    yield palindrome
            else:
                palindrome = int(first + last)
                yield palindrome
        current_places += 1


def is_palindrome(n: int) -> bool:
    """Predicate is true, if the decimal representation of n is a number palindrome."""
    if not isinstance(n, int):
        raise TypeError('This predicate requires an int argument.')
    if not n > 0:
        raise ValueError('The argument value must be a positive number.')
    s = str(n)
    return s == s[::-1]


def is_bitwise_palindrome(n):
    """Predicate is true, if the bit representation of n is a number palindrome."""
    if not isinstance(n, int):
        raise TypeError('This predicate requires an int argument.')
    if not n > 0:
        raise ValueError('The argument value must be a positive number.')
    s = bin(n)[2:]
    return s == s[::-1]


def is_permutation(j, k):
    if not (isinstance(j, int) and isinstance(k, int)):
        raise TypeError('Predicate requires two int arguments.')
    if not (j >= 0 and k >= 0):
        raise ValueError('Both arguments must be positive numbers.')
    return sorted(str(j)) == sorted(str(k))


def triangular(n: int) -> int:
    return n * (n + 1) // 2


def triangular_numbers():
    n = 1
    triangular_number = n
    while True:
        yield triangular_number
        n += 1
        triangular_number += n


def fibonacci_series():
    """This generator provides an infinite series. Does not return. Yields forever.
    Be sure, when used in a for loop, to provide a limiting decision in the loop.
    Be aware: The index of the first fibonacci number is 1, the second is 2, then 3, etc.
    """
    f1, f2 = 1, 1
    yield f1
    while True:
        yield f2
        f1, f2 = f2, f1 + f2


def fibonacci_series_m(m=10 ** 9):
    """This generator provides an infinite series. Does not return. Yields forever.
    Be sure, when used in a for loop, to provide a limiting decision in the loop.
    Be aware: The index of the first fibonacci number is 1, the second is 2, then 3, etc.
    """
    f1, f2 = 1, 1
    yield f1
    while True:
        yield f2
        f1, f2 = f2, (f1 + f2) % m


def is_pentagonal(n: int) -> bool:
    """To decide if n is a pentagonal number, we solve ((24n +1)^0.5 + 1) / 6.
    Afterwards we pick that solution and test if it is a positive integer. If so, n must be
    pentagonal. Otherwise n is not pentagonal. (In fact, our successful pick than gives the P_n
    index of that pentagonal number. But we're not gonna use that property yet.)

    The predicate returns True (is_pentagonal) or False (is_not_pentagonal).

    Be aware, n must be a positive number to get a non-nonsense result. Negative "extended"
    pentagonal numbers can not be recognized with this predicate.
    """
    p = (sqrt(24 * n + 1) + 1) / 6
    return p == int(p)


def is_generalized_pentagonal(n: int) -> bool:
    sq = sqrt(24 * n + 1)
    return sq == int(sq)


def pentagonal(n: int) -> int:
    """Returns the n_th pentagonal number. If fed with a negative number, it returns an
    extended pentagonal number.
    """
    return n * (3 * n - 1) // 2


def partition(number: int) -> int:
    """Calculates the number of partitions, a given number may have, by using Euler's
    recursive partition function, which makes use of generalized pentagonal numbers.

    part(n) = SUM(k!=0, Pn > n, sgn * part(n - Pn))

    Without further measure, the greatest n we can recursively calculate the number of
    partitions for, is currently n=993 (due to max. recursion depth).
    """
    memo = {}

    def partition_(n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n in memo:
            return memo[n]
        sign, result = 1, 0
        for k in range(1, n + 1):
            a = n - pentagonal(k)
            term_a = 0
            if a >= 0:
                term_a = partition_(a)
                memo[a] = term_a
            b = n - pentagonal(-k)
            term_b = 0
            if b >= 0:
                term_b = partition_(b)
                memo[b] = term_b
            result = result + sign * (term_a + term_b)
            sign = -sign
        return result

    return partition_(number)


def hexagonal(n: int) -> int:
    return n * (2 * n - 1)


def is_hexagonal(n):
    x = (1 + (1 + 8 * n) ** 0.5) / 4
    return x == int(x)


def is_pandigital(n, start=1, stop=9):
    s = str(n)
    return all(map(lambda x: x in s, '0123456789'[start:stop + 1])) and len(s) == 9


if __name__ == '__main__':
    print('Result is', star_lcm(range(2, 20 + 1)))

# last line of code
