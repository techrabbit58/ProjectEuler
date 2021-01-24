"""This solves problem #30 of Project Euler (https://projecteuler.net).

Surprisingly there are only three numbers that can be written as the sum of fourth powers of
their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def explode(n):
    return tuple(map(int, tuple(str(n))))


def sum_of_digit_powers(digits, power):
    return sum(map(lambda x: x ** power, digits))


def attempt():
    """Finding the interval is the key, when searching for all possible digit power sum
    identities.

    For the lower bound, since a single digit^5 is not a sum, we take at least two digits.

    The highest possible number that can be summed up to meet the constraint, is 5 * 9^5
    (a six digit number). We can take 6 * 9^5 to be on the safe side, and take this for the
    bounds.
    """
    power = 5
    result = 0
    from math import log10
    for n in range(2, (1 + round(log10(9 ** power))) * 9 ** power):
        digits = explode(n)
        product_ = sum_of_digit_powers(digits, power)
        if n == product_:
            print(n, digits)
            result += n
    return result


def run_application():
    import time

    start = time.time()
    solution = attempt()
    elapsed = time.time() - start

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
