"""This solves problem #493 of Project Euler (https://projecteuler.net).
Under The Rainbow
Problem 493

70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.

What is the expected number of distinct colours in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
import random
from collections import Counter, defaultdict

from helpers import chronometric
from mathext import binomial


def initialize():
    urn = []
    for n in range(1, 8):
        urn += [n] * 10
    return urn


def draw(urn, takes):
    result = []
    for _ in range(takes):
        random.shuffle(urn)
        result.append(urn.pop())
    return result[:]


def monte_carlo(rounds):
    urn = initialize()
    results = defaultdict(int)
    for _ in range(rounds):
        results[len(Counter(draw(urn[:], 20)))] += 1
    results = {k: v / rounds for k, v in results.items()}
    print(results)
    x = 0
    for k, v in results.items():
        x += k * v
    print('Approximate expectation =', x)


@chronometric
def under_the_rainbow():
    """The Monte Carlo approach showed that the solution must be somewhere around
    6.82 so that sometimes one color is not drawn. To calculate the probabilities for all
    possible draws is very complicated. So someone on the internet suggested to calculate
    the probability for any color probably not to be drawn. Which is much easier.
    Not to draw one color means, only to choose from the other 60 balls.

    After having solved this way, I found the following of user 'tepsi' explanation in the
    forum:

    For any given colour, the probability of it being present in the draw is

        p= 1 − nCr(60, 20) / nCr(70, 20).

    The expected value of the number of colours present is just the sum of the expected
    values of the number of occurrences of the individual colours, which are all equal to p
    (0 with probability 1−p, 1 with probability p), so the total expectation value
    is 7p.

    Sigh!
    """
    monte_carlo(1000)
    return 7 * (1 - binomial(60, 20) / binomial(70, 20))


def run_application():
    solution, elapsed = under_the_rainbow()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
