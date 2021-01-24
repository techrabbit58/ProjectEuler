"""This solves problem #20 of Project Euler (https://projecteuler.net).

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def first_attempt(*, n=10):
    from math import factorial
    print(sum(map(int, list(str(factorial(n))))))


def run_application():
    import time
    start = time.time()
    first_attempt(n=100)
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
