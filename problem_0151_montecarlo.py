"""This doesn't solve problem #151 of Project Euler (https://projecteuler.net).

A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special
colour-proofing paper of size A5.

Every Monday morning, the foreman opens a new envelope, containing a large sheet of the
special paper with size A1.

He proceeds to cut it in half, thus getting two sheets of size A2. Then he cuts one of them
in half to get two sheets of size A3 and so on until he obtains the A5-size sheet needed for
the first batch of the week.

All the unused sheets are placed back in the envelope.

At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at
random. If it is of size A5, he uses it. If it is larger, he repeats the 'cut-in-half'
procedure until he has what he needs and any remaining sheets are always placed back in the
envelope.

Excluding the first and last batch of the week, find the expected number of times (during
each week) that the foreman finds a single sheet of paper in the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx .

B.t.w.: This given solution enumerates all possible envelope content and provides only the
"good" results. These are returned one by one and then get accumulated to give the final
solution. It runs for milliseconds when I start with A2, but for more than an hour if I start
with A1. There must be a better way.

B.t.w.: the Monte Carlo approach, by simulating 100 million weeks, runs for hours but is
accurate to only 4 decimal places. It does not produce a good solution within reasonable time.

B.t.w.: to enumerate all possible outcomes is pointless as well, and leads to a memory
error after batch #13. Although there might be some tuning possible, so that it can complete,
completion will take forever. There must be a better way.
"""

batches_to_run = 16

cut = {
    'A1': ['A2'] * 2,
    'A2': ['A3'] * 2,
    'A3': ['A4'] * 2,
    'A4': ['A5'] * 2
}


def simulate_one_week():
    import random

    envelope = ['A1']

    found_only_one_sheet = 0

    for batch in range(1, batches_to_run + 1):
        random.shuffle(envelope)
        if len(envelope) == 1 and batch != 1 and batch != batches_to_run:
            found_only_one_sheet += 1
        sheet = envelope.pop()
        while sheet != 'A5':
            sheets = cut[sheet]
            envelope.append(sheets[0])
            sheet = sheets[1]

    return found_only_one_sheet


def monte_carlo_attempt(weeks_to_go):
    from collections import Counter
    outcomes = Counter()
    for r in range(weeks_to_go):
        outcomes[simulate_one_week() > 0] += 1
        if r % 50_000 == 1:
            print(r, round(outcomes[True] / r, 6))
    print('expect one sheet at', round(outcomes[True] / weeks_to_go, 6), 'batches a week')


def run_application():
    import time
    start = time.time()
    monte_carlo_attempt(100_000_000)
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
