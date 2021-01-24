"""This solves problem #70 of Project Euler (https://projecteuler.net).

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the
number of positive numbers less than or equal to n which are relatively prime to n. For
example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n)
produces a minimum.
"""

from mathext import euler_phi, is_permutation


def totient_ratio(n, phi):
    return n / phi


def attempt():
    limit = 10 ** 7
    min_phi_ratio = totient_ratio(2, euler_phi(2))
    for n in range(2, limit):
        phi = euler_phi(n)
        if is_permutation(n, phi):
            r = totient_ratio(n, phi)
            if min_phi_ratio > r:
                min_phi_ratio = r
                print(n, phi, r)


def run_application():
    import time
    start = time.time()
    attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
