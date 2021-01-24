"""This solves problem #69 of Project Euler (https://projecteuler.net).

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the
number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7,
and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n 	Relatively Prime 	φ(n) 	n/φ(n)

2 	1	                1       2
3 	1,2                 2       1.5
4 	1,3                 2       2
5 	1,2,3,4             4       1.25
6 	1,5                 2       3
7 	1,2,3,4,5,6         6       1.1666...
8 	1,3,5,7             4       2
9 	1,2,4,5,7,8         6       1.5
10 	1,3,7,9             4       2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

from mathext import euler_phi


def totient_ratio(n):
    return n / euler_phi(n)


def attempt(*, limit=10):
    """Find the number in [2 ... limit] that has the highest phi ratio."""
    has_maximum_phi_ratio = (2, totient_ratio(2))
    for n in range(2, limit + 1):
        q = totient_ratio(n)
        if q > has_maximum_phi_ratio[1]:
            has_maximum_phi_ratio = (n, q)
            print(has_maximum_phi_ratio[0], '=>', has_maximum_phi_ratio[1])


def run_application():
    import time
    start = time.time()
    attempt(limit=1_000_000)
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
