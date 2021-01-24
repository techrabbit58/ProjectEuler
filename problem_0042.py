"""This solves problem #42 of Project Euler (https://projecteuler.net).

Coded triangle numbers

The nth term of the sequence of triangle numbers is given by, t_n = n(n+1)/2; so the first ten
triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. For example, the word value for SKY is 19 + 11
+ 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a
triangle word.

Using p042_words.txt, a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
"""

import json

from mathext import triangular_numbers


def word_value(word):
    from string import ascii_uppercase
    return sum(ascii_uppercase.index(c) + 1 for c in word.upper())


def is_triangle_number(n):
    for k in triangular_numbers():
        if k == n:
            return True
        elif k > n:
            return False
        else:
            continue


def attempt(*, input_file_name='p042_words.txt'):

    with open(input_file_name) as fp:
        words = json.loads('[' + fp.read() + ']')

    number_of_triangle_words = 0
    for word in words:
        if is_triangle_number(word_value(word)):
            number_of_triangle_words += 1

    return number_of_triangle_words


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
