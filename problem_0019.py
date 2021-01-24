"""This solves problem #19 of Project Euler (https://projecteuler.net).

You are given the following information, but you may prefer to do some research for yourself.

    o   1 Jan 1900 was a Monday.
    o   Thirty days has September,
    o   April, June and November.
    o   All the rest have thirty-one,
    o   Saving February alone,
    o   Which has twenty-eight, rain or shine.
    o   And on leap years, twenty-nine.
    o   A leap year occurs on any year evenly divisible by 4, but not on a century unless it
        is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to
31 Dec 2000)?
"""

import calendar


def first_attempt():
    result = 0
    for year in range(1901, 2000 + 1):
        for month in range(1, 12 + 1):
            if calendar.monthrange(year, month)[0] == calendar.SUNDAY:
                result += 1
    print('During the twentieth century (1 Jan 1901 to 31 Dec 2000),')
    print(result, 'Sundays fell on the first of the month.')


def run_application():
    import time
    start = time.time()
    first_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
