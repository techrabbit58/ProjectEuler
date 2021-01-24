"""This solves problem #38 of Project Euler (https://projecteuler.net).

Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576
the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(n):
    return '123456789' == ''.join(sorted(str(n)))


def concatenate_multiples(n, *, places):
    k = 2
    result = str(n)
    while len(result) < places:
        result += str(n * k)
        k += 1
    return int(result)


def attempt():
    maximum = 0
    for n in range(2, 9876 + 1):
        product = concatenate_multiples(n, places=9)
        if is_pandigital(product) and product > maximum:
            maximum = product
    return maximum


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
