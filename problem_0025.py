"""
1000-digit Fibonacci number
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from mathext import fibonacci_series


def attempt(*, limit=3):
    """This straight forward attempt is useful up to approximately index 1000.
    Above this index, it tends to become annoyingly slow.

    The implementation builds on a generator enumerating all Fibonacci numbers to infinity.
    """
    for index, f in enumerate(fibonacci_series(), 1):
        if not (len(str(f)) < limit):
            print('Solution =', index)
            break


if __name__ == '__main__':
    import time
    start = time.time()
    attempt(limit=1000)
    print('Elapsed:', time.time() - start, 'seconds')

# last line of code
