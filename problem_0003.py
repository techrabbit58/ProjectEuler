"""This solves problem #3 of Project Euler (https://projecteuler.net)

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

"""

from collections import Counter

from mathext import prime_number_generator


def run_solution(n=13195):

    prime = prime_number_generator()

    factors = []

    p = next(prime)
    while n > 1:
        while (n % p) == 0:
            n //= p
            factors.append(p)
        p = next(prime)

    counter = Counter(factors)

    print('all prime factors:', counter)
    print('maximum prime factor:', max(counter))


if __name__ == '__main__':
    run_solution(600851475143)

# last line of code
