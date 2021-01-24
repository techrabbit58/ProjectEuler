"""This solves problem #57 of Project Euler (https://projecteuler.net).

Square root convergents
Problem 57

It is possible to show that the square root of two can be expressed as an infinite continued
fraction.

    sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion,
1393/985, is the first example where the number of digits in the numerator exceeds the number
of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits
than denominator?
"""
from fractions import Fraction

from helpers import chronometric


def chained_fractions():
    """Generate the fractional part for the approximation of sqrt(2) with increasing
    precision. Begin with Fraction('1/2') and then follow the rule:

    denominator(n + 1) = 2 * denominator(n) + numerator(n)
    numerator(n + 1) = denominator(n)

    yield Fraction(numerator(n + 1), denominator(n + 1))

    on each iteration.
    """
    numerator, denominator = 1, 2
    while True:
        yield Fraction(numerator, denominator)
        numerator, denominator = denominator, 2 * denominator + numerator


def is_abundant_numerator(frac: Fraction) -> bool:
    """Compqares the number of decimal places of the numerator and denominator of the given
    fraction.

    Returns True if the numerator has more places than the denominator.
    Returns False, if not.
    """
    return len(str(frac.numerator)) > len(str(frac.denominator))


@chronometric
def attempt():
    abundant_approximations = 0
    for n, m in enumerate(chained_fractions(), start=1):
        if n <= 1000:
            if is_abundant_numerator(Fraction('1') + m):
                abundant_approximations += 1
        else:
            break
    return abundant_approximations


def run_application():
    solution, elapsed = attempt()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
