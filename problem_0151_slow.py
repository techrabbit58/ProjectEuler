"""This solves problem #151 of Project Euler (https://projecteuler.net).

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

B.t.w.: the Monte Carlo approach, by simulating 100 million weeks, runs for hours but is
accurate to only 4 decimal places. It does not produce a good solution within reasonable time.

To enumerate all possible outcomes is pointless as well, and leads to a memory
error after batch #13. Although there might be some tuning possible, so that it can complete,
completion will take forever. There must be a better way.
"""

from collections import namedtuple

Envelope = namedtuple('Envelope', 'predictand content batch')

A1, A2, A3, A4, A5 = 1, 2, 3, 4, 5


def cut_sheet(single_sheet):
    if single_sheet not in range(A1, A5 + 1):
        raise ValueError(
            'single sheet {} not in range A1 ... A5'.format('A{}'.format(single_sheet)))
    return (A1, A2, A3, A4, A5)[single_sheet:]


def next_batches(predictand, content, batch):
    sheets = len(content)
    if sheets == 0:
        return
    if sheets == 1 and content[0] in (A2, A3, A4):
        yield Envelope(predictand, content, batch)
        yield from next_batches(predictand, cut_sheet(content[0]), batch + 1)
    else:
        for index, sheet in enumerate(content):
            yield from next_batches(predictand * 1 / sheets, content[:index] + cut_sheet(
                sheet) + content[index + 1:], batch + 1)


def attempt():
    solution = 0
    for envelope in next_batches(1.0, cut_sheet(A1), 1):
        solution += envelope.predictand
    print('Solution =', round(solution, 6))


def run_application():
    import time
    start = time.time()
    attempt()
    print('Runtime =', (time.time() - start), 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
