"""This solves problem #233 of Project Euler (https://projecteuler.net).

Lattice points on a circle
Problem 233

Let f(N) be the number of points with integer coordinates that are on a circle passing
through (0,0), (N,0),(0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?
"""

from helpers import chronometric

START = 359125
LIMIT = 469625
CRITERIA = 420


@chronometric
def lattice_points_on_a_circle():
    # TODO: Find the solution. This is not the solution.
    sqrt2 = 2 ** 0.5
    expansion_factor = 1 + sqrt2
    for n in range(START, LIMIT + 1):
        two_n_squared = (n ** 2) << 1
        max_y = int(n * expansion_factor / 2)
        lattice_points = 4
        for y in range(n + 1, max_y + 1):
            delta_y_squared = ((y << 1) - n) ** 2
            delta_x_squared = two_n_squared - delta_y_squared
            if not (delta_x_squared + delta_y_squared) & 1:
                delta_x = delta_x_squared ** 0.5
                if delta_x == int(delta_x):
                    lattice_points += 8
        if lattice_points == CRITERIA:
            print(n, max_y)
    return None


def run_application():
    solution, elapsed = lattice_points_on_a_circle()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code

"""
271204031455541309
"""
