"""This solves problem #49 of Project Euler (https://projecteuler.net).

Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from collections import defaultdict
from itertools import permutations, dropwhile, takewhile
from math import log10

from helpers import chronometric
from mathext import prime_number_generator, is_prime


@chronometric
def attempt():
    four_digit_primes = primes_range(1000, 10000)
    solution = set()
    for prime in four_digit_primes:
        candidates = generate_candidates_from_prime(prime)
        if len(candidates) >= 3:
            distances = create_distance_matrix(candidates)
            if len(distances) > 0:
                distances = filter_distance_matrix(distances)
                for elements in distances.values():
                    solution.add(make_twelve_digit_number(elements))
    return solution


def primes_range(start, stop):
    primes = []
    for p in takewhile(
            lambda x: x < stop,
            dropwhile(
                lambda y: y <= start,
                prime_number_generator())):
        primes.append(p)
    return primes


def generate_candidates_from_prime(prime):
    candidates = set()
    for candidate in permutations(str(prime)):
        candidate = int(''.join(candidate))
        if is_prime(candidate) and log10(candidate) >= 3:
            candidates.add(candidate)
    return candidates


def create_distance_matrix(candidates):
    distances = defaultdict(set)
    for j in candidates:
        for k in candidates:
            diff = abs(j - k)
            if diff > 0:
                distances[diff].update({j, k})
    return distances


def filter_distance_matrix(distances):
    distances = {distance: sorted(elements)
                 for distance, elements in distances.items()
                 if len(elements) == 3
                 }
    return distances


def make_twelve_digit_number(elements):
    twelve_digit_number = int('{}{}{}'.format(*elements))
    return twelve_digit_number


def run_application():
    solution, elapsed = attempt()

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
