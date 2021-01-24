"""This solves problem #33 of Project Euler (https://projecteuler.net).

Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of
the denominator.
"""

from fractions import Fraction
from math import gcd

from helpers import chronometric


class Application:

    @staticmethod
    def is_trivial(numerator, denominator):
        return numerator % 10 == 0 and denominator % 10 == 0

    @staticmethod
    def cancel_digits(numerator, denominator):
        result = []
        numerator_digits = set(str(numerator))
        denominator_digits = set(str(denominator))
        if numerator_digits.isdisjoint(denominator_digits):
            return result
        cancellable_digits = (d for d in numerator_digits.intersection(denominator_digits))
        for k in cancellable_digits:
            n, d = list(str(numerator)), list(str(denominator))
            n.remove(k)
            d.remove(k)
            n, d = int(n[0]), int(d[0])
            if n != 0 and d != 0 and n < d:
                result.append((n, d))
        return result

    @chronometric
    def digit_cancelling_fractions(self):
        result = Fraction(1, 1)
        for denominator in range(11, 100):
            for numerator in range(10, denominator):
                if self.is_trivial(numerator, denominator):
                    continue
                if gcd(numerator, denominator) == 1:
                    continue
                cancelling_fractions = self.cancel_digits(numerator, denominator)
                if len(cancelling_fractions) > 0:
                    for cf in cancelling_fractions:
                        s = Fraction('/'.join(str(c) for c in cf))
                        f = Fraction(numerator, denominator)
                        if s == f:
                            result *= f
        return result.denominator

    def run(self):

        solution, elapsed = self.digit_cancelling_fractions()

        print('Solution =', solution)
        print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    Application().run()

# last line of code
