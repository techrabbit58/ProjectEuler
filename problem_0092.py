"""This solves problem #92 of Project Euler (https://projecteuler.net).

Square digit chains
Problem 92

A number chain is created by continuously adding the square of the digits in a number to form
a new number until it has been seen before.

For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is
most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

B.t.w.: All numbers arriving at one this way are also caled "Happy Numbers". Exploiting the
Happy Numbers may lead to a much faster solution. E.g. the "Happy Number" property being
independent of rearrangement of the cipher sequence (i.e. digital permutaions).
"""
from helpers import chronometric

LIMIT = 10**7

MAGIC_NUMBERS = {1, 89}
CRITERIA = 89

DIGIT_SQUARES = {str(n): pow(n, 2) for n in range(10)}

MEMORY = {1: 1, 89: 89}


def _next_square_digit_sum(n):
    if n in MEMORY:
        return MEMORY[n]
    return sum(DIGIT_SQUARES[c] for c in str(n))


def square_digit_chain(n):
    chain_link = n
    while chain_link not in MAGIC_NUMBERS:
        chain_link = _next_square_digit_sum(chain_link)
    MEMORY[n] = chain_link
    return chain_link


@chronometric
def square_digit_chains():
    result = 0
    for n in range(1, LIMIT):
        chain_result = square_digit_chain(n)
        if chain_result == CRITERIA:
            result += 1
    return result


def run_application():
    solution, elapsed = square_digit_chains()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
