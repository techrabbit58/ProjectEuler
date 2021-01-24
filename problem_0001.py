"""Problem 1 from Project Euler (projecteuler.net)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5,
6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

from mathext import gauss_sum


def run_solution(*, limit):
    result = 3 * gauss_sum((limit - 1) // 3)
    result += 5 * gauss_sum((limit - 1) // 5)
    result -= 15 * gauss_sum((limit - 1) // 15)
    return result


if __name__ == '__main__':
    print('Starting calculation ...')
    start = time.time()
    print('Solution =', run_solution(limit=1000))
    print('Runtime =', time.time() - start, 'seconds')
    print('Done.')

# last line of code
