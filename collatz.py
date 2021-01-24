"""A naive implementation of the Collatz series, and some Collatz utilities.

B.t.w., this also solves problem 14 of Project Euler (https://projecteuler.net).
"""
import time
from functools import lru_cache

ERROR_MSG = 'arg must be a positive whole number'


def _collatz_next_number(n):
    """Given a non negative whole number:

    Return n // 2 if n is equal.
    Return 3 * n + 1 otherwise.

    Throw an error, if n <= 0 or n is not an integer.
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


@lru_cache(maxsize=None)
def collatz_len(n):
    """Given a non negative whole number,

    return the length of the Collatz series of that number
        including this number itself.

    CAVEAT: This is a recursive function! Be aware, that there
    is currently no mathematical evidence that Collatz does
    drill down to 1 for every given N.

    Examples:
        collatz_len(1) == 1
        collatz_len(4) == 3
        collatz_len(13) == 10
        collatz_len(26) == 1 + collatz_len(13) == 11
    """
    if not (isinstance(n, int) and n > 0):
        raise ValueError(ERROR_MSG)
    if n == 1:
        return 1
    else:
        return 1 + collatz_len(_collatz_next_number(n))


def collatz(n):
    """Calculate a list of the Collatz series for a given natural number.

    Return the list of numbers from the Collatz series (without the
    originating n).
    """
    if not (isinstance(n, int) and n > 0):
        raise ValueError(ERROR_MSG)
    numbers = []
    while n > 1:
        n = _collatz_next_number(n)
        numbers.append(n)
    return numbers


def collatz_ex(n):
    """Calculate a list of the Collatz series for a given natural number.

    Return the list of numbers from the Collatz series,
        but with n as first element.
    """
    return [n] + collatz(n)


def collatz_max_length(*bounds):
    collatz_num = 0
    max_length = 0
    for n in range(*bounds):
        length = collatz_len(n)
        if length > max_length:
            collatz_num = n
            max_length = length
    return collatz_num, max_length


if __name__ == '__main__':
    start = time.time()
    print(collatz_max_length(1, 1_000_000))
    print('runtime =', (time.time() - start), 'seconds')

# last line of code
