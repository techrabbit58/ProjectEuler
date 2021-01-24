"""This solves problem #65 of Project Euler (https://projecteuler.net).

Convergents of e
Problem 65

The square root of 2 can be written as an infinite continued fraction.

    sqrt(2) = 1+1/(2+1/(2+1/(2+1/(2+...))))

The infinite continued fraction can be written, sqrt(2)=[1;(2)],
(2) indicates that 2 repeats ad infinitum. In a similar way, sqrt(23)=[4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots
provide the best rational approximations.

Hence the sequence of the first ten convergents for sqrt(2) are:

    1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,

    e=[2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...].

The first ten terms in the sequence of convergents for e are:

    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent
of the continued fraction for e.
"""

from helpers import chronometric
from mathext import reversed_euklid, digit_sum


def prepare_quotient_list(length):
    chain_fraction_e = [2]
    for n in range(2, length, 2):
        chain_fraction_e += [1, n, 1]
    return chain_fraction_e[:length]


@chronometric
def convergents_of_e():
    length = 100
    chain_fraction = prepare_quotient_list(length)
    approximation = reversed_euklid(chain_fraction)
    return digit_sum(approximation.numerator)


def run_application():
    solution, elapsed = convergents_of_e()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
