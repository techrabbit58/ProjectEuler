"""This solves problem #13 of Project Euler (https://projecteuler.net).

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

    (Please read file p013_numbers.txt for the numbers.)

"""

NUMBERS = 'p013_numbers.txt'


def parse_numbers_file(file_name):
    with open(file_name) as fp:
        numbers = fp.readlines()
    return (int(n) for n in numbers)


def first_attempt():
    numbers = parse_numbers_file(NUMBERS)
    from itertools import accumulate
    print(str(list(accumulate(numbers))[-1])[:10])


def run_application():
    import time
    start = time.time()
    first_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
