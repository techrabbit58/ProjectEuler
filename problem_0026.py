"""This solves problem #26 of Project Euler (https://projecteuler.net).

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7
has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
"""


def first_attempt():
    import requests
    url_with_helpful_data = 'https://oeis.org/A051626/b051626.txt'
    max_repetend_length = 0
    for line in requests.get(url_with_helpful_data).text.splitlines():
        n, repetend_length = map(int, line.split())
        if n >= 1000:
            break
        if repetend_length > max_repetend_length:
            max_repetend_length = repetend_length
            d = n
    print('Solution =', d)


def run_application():
    import time
    start = time.time()
    first_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
