"""This solves problem #21 of Project Euler (https://projecteuler.net).

Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide
evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b
are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from mathext import sigma_star


def attempt(*, start=220, limit):
    divisor_sums = {}
    amicable_numbers = set()
    for n in range(start, limit):
        divisor_sums.setdefault(sigma_star(n), []).append(n)
    for divisor_sum in divisor_sums:
        for n in divisor_sums[divisor_sum]:
            if n != divisor_sum and n in divisor_sums and divisor_sum in divisor_sums[n]:
                amicable_numbers.update({divisor_sum, n})
    return amicable_numbers


def run_application():
    import time
    start = time.time()
    amicable_numbers = attempt(limit=10_000)
    elapsed = time.time() - start
    print('Amicable Numbers:', sorted(amicable_numbers))
    print('Solution =', sum(amicable_numbers))
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
