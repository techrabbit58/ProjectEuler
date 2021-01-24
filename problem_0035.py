"""This solves problem #35 of Project Euler (https://projecteuler.net).

Circular primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971,
and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from mathext import prime_number_generator


def find_primes(*, up_to=100):
    primes = []
    for p in prime_number_generator():
        if p >= up_to:
            break
        primes.append(p)
    return primes


def rotations(n):
    result = []
    digits = str(n)
    for _ in range(len(digits)):
        digits = digits[-1] + digits[:-1]
        result.append(int(digits))
    return result


def first_attempt():
    primes = set(find_primes(up_to=1_000_000))
    circular_primes = set()
    for p in primes:
        r = rotations(p)
        if any(map(lambda k: k in circular_primes, r)):
            continue
        if all(map(lambda k: k in primes, r)):
            circular_primes.update(r)
    print(sorted(circular_primes))
    print('Solution =', len(circular_primes))


def run_application():
    import time
    start = time.time()
    first_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
