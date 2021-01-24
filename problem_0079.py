"""This solves problem #79 of Project Euler (https://projecteuler.net).

Passcode derivation
Problem 79

A common security method used for online banking is to ask the user for three random
characters from a passcode. For example, if the passcode was 531278, they may ask for the
2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to
determine the shortest possible secret passcode of unknown length.
"""

from helpers import chronometric


@chronometric
def derive_passcode(key_log='p079_keylog.txt'):
    """Derive shortest passcode from the logfile that has recorded 50 successful attempts.
    1) Read and parse logfile.
    2) Analyse all available symbols, and which symbols have which predecessors.
    3) Determine the set of start symbols.
    4) For every start symbol, find the shortest possible sequence.
    5) Chose the shortest possible passcode as the solution and return this to the caller.
    """
    attempts = read_and_parse(key_log)
    passcode_digits, predecessors = analyse_all_attempts(attempts)
    start_symbols = passcode_digits ^ predecessors.keys()
    passcodes = []
    for start_symbol in start_symbols:
        passcodes.append(shortest_sequence(predecessors, start_symbol))
    return ''.join(min(passcodes, key=lambda x: len(x)))


def shortest_sequence(predecessors, start_symbol):
    """  CAVEAT! Will enter an infinite loop if topology contains loops.
    Can not deal with equal length sequences. Just good enough for the #79 case.
    Might not give satisfying results with sequences that contain repeated symbols.
    """
    sequence = [start_symbol]
    while True:
        candidates = [k for k, v in predecessors.items() if sequence[-1] in v]
        if not candidates:
            break
        elected = min(candidates, key=lambda x: len(predecessors[x]))
        sequence.append(elected)
    return sequence


def analyse_all_attempts(attempts):
    from collections import defaultdict
    passcode_digits = set()
    predecessors = defaultdict(set)
    for attempt in attempts:
        predecessors[attempt[-1]].update(attempt[:2])
        predecessors[attempt[-2]].add(attempt[0])
        passcode_digits.update(attempt)
    return passcode_digits, predecessors


def read_and_parse(key_log):
    with open(key_log) as fp:
        attempts = fp.read().strip().splitlines()
    return attempts


def run_application():
    solution, elapsed = derive_passcode()
    print('Solution =', solution)
    print('Runtime =', elapsed, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
