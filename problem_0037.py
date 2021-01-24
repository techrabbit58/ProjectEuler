"""This solves problem #37 of Project Euler (https://projecteuler.net).

Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible to
continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97,
and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right
to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from mathext import prime_number_generator, is_prime


def find_all_trunks(number):
    trunks = set()
    divisor = 1
    while divisor < number:
        divisor *= 10
        trunks.update(divmod(number, divisor))
    trunks.remove(0)
    return trunks


def attempt():

    max_truncatable_primes = 11
    truncatable_primes = []

    for prime in prime_number_generator():

        if len(truncatable_primes) >= max_truncatable_primes:
            break

        if prime < 10:
            continue

        trunks = find_all_trunks(prime)

        if all(map(is_prime, trunks)):
            print('prime =', prime, ', trunks =', list(sorted(trunks)))
            truncatable_primes.append(prime)

    return sum(truncatable_primes)


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
