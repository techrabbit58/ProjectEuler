"""This solves problem #31 of Project Euler (https://projecteuler.net).

In England the currency is made up of pound, £, and pence, p, and there are eight coins in
general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

import time


def calculate_ways_to_make(*, amount=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways_to_make = [1 for _ in range(amount + 1)]
    for coin in sorted(coins[1:]):
        for a in range(coin, amount + 1):
            ways_to_make[a] += ways_to_make[a - coin]
    return ways_to_make[-1]


def run_application():
    amount = 200
    start = time.time()
    print(
        'Ways to make £{} from british coins: {}.'.format(
            amount / 100, calculate_ways_to_make(amount=amount)))
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
