"""Common helpful routines for Project Euler solutions."""

import time
from functools import wraps


def chronometric(function):
    """A decorator that allows timed run of the wrapped function.
    Returns a function providing the result of the wrapped function, together with the time 
    elapsed for running the function, as a tuple (function_result, runtime).
    """

    @wraps(function)
    def wrapped(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return result, elapsed

    return wrapped


def inclusive_range(a, b=None, step=1):
    if b is None:
        return range(1 + a)
    else:
        return range(a, 1 + b, step)


# last line of code
