"""This solves problem #89 of Project Euler (https://projecteuler.net).

For a number written in Roman numerals to be considered valid there are basic rules which
must be followed. Even though the rules allow some numbers to be expressed in more than one
way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII                 (valid)
    VVVI
    XVI                     (valid)

However, according to the rules only XIIIIII and XVI are valid, and the last example is
considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, p089_roman.txt, contains one  thousand numbers written in valid,
but not necessarily minimal, Roman numerals.

Traditional Roman numerals are made up of the following denominations:

    I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

- Numerals must be arranged in descending order of size.
- M, C, and X cannot be equalled or exceeded by smaller denominations.
- D, L, and V can each only appear once.

In addition to the three rules given above, if subtractive combinations are used then the
following four rules must be followed.

- Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
- I can only be placed before V and X.
- X can only be placed before L and C.
- C can only be placed before D and M.

It is also expected, but not required, that higher denominations should be used whenever
possible.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four
consecutive identical units.
"""

from roman_numbers import decimal_to_roman, relaxed_roman_to_decimal

NUMBERS = 'p089_roman.txt'


def read_file(fn):
    with open(fn) as fp:
        numbers = (line.strip() for line in fp.readlines())
    return numbers


def optimized(rn):
    return decimal_to_roman(relaxed_roman_to_decimal(rn))


def attempt():
    numbers = read_file(NUMBERS)

    saved_characters = 0
    for roman_number in numbers:
        pre_length = len(roman_number)
        rn = optimized(roman_number)
        post_length = len(rn)
        saved_characters += (pre_length - post_length)

    print('Solution =', saved_characters)


def run_application():
    import time
    start = time.time()
    attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
