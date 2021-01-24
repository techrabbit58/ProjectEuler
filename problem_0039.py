"""This solves problem #39 of Project Euler (https://projecteuler.net).

Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

        {20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Some observations:

    (p - q)^2 + 4pq = (p + q)^2

    p = u^2, q = v^2

    (u^2 - v^2)^2 + (2uv)^2 = (u^2 + v^2)^2

    u^2 - v^2 = a, 2uv = b, u^2 + v^2 = c

    a^2 + b^2 = c^2

    n = a + b + c = u^2 - v^2 + 2uv + u^2 + v^2 = 2(u*u + u*v) = 2 * u * (u + v)

    n must be even!
"""


def solution_for_perimeter(perimeter):
    result = 0
    pa = 1 + perimeter // 3
    pb = 1 + 2 * perimeter // 3
    pc = 1 + perimeter
    for a in range(1, pa):
        for b in range(a + 1, pb):
            ab = a + b
            aabb = a**2 + b**2
            for c in range(b + 1, pc):
                if perimeter == ab + c and aabb == c**2:
                    result += 1
                else:
                    continue
    return result


def attempt():
    maximum = 0
    solution = None
    for perimeter in range(2, 1000 + 1, 2):
        triangles = solution_for_perimeter(perimeter)
        if triangles > maximum:
            maximum = triangles
            solution = perimeter
            print(perimeter, triangles)
    return solution


def run_application():
    import time

    start = time.time()
    solution = attempt()
    elapsed = time.time() - start

    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
