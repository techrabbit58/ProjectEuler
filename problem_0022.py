"""This solves problem #22 of Project Euler (https://projecteuler.net).

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting
it into alphabetical order. Then working out the alphabetical value for each name, multiply
this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 +
12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 =
49714.

What is the total of all the name scores in the file?
"""

import time
from string import ascii_uppercase


def read_file(fn):
    with open(fn) as fp:
        raw_words = fp.read().replace('"', '').split(',')
    return raw_words


def alpha_value(word):
    result = 0
    for c in word.upper():
        result += ascii_uppercase.find(c) + 1
    return result


def run_exercise(*, fn='names.txt'):
    result = 0
    for i, w in enumerate(sorted(read_file(fn))):
        result += (alpha_value(w) * (i + 1))
    print('Names score =', result)


if __name__ == '__main__':
    print('Running exercise ...')
    start = time.time()
    run_exercise()
    print('Runtime =', time.time() - start, 'seconds')
    print('Done.')

# last line of code
