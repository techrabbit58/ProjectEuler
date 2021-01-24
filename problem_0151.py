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
"""

from collections import Counter, namedtuple

A1, A2, A3, A4, A5 = 1, 2, 3, 4, 5

Envelope = namedtuple('Envelope', 'predictand content')

outcomes = (Counter((A2, )), Counter((A3, )), Counter((A4, )))


def cut_sheet(single_sheet):
    if single_sheet not in range(A1, A5 + 1):
        raise ValueError(
            'single sheet {} not in range A1 ... A5'.format('A{}'.format(single_sheet)))
    return (A1, A2, A3, A4, A5)[single_sheet:]


def next_envelope(envelope, sheet):
    return envelope - Counter((sheet, )) + Counter(cut_sheet(sheet))


def num_sheets(envelope):
    return sum(envelope.values())


def next_batches(predictand, content):
    sheets = num_sheets(content)
    if sheets == 0:
        return
    if content in outcomes:
        yield Envelope(predictand, content)
        sheet = list(content.keys())[0]
        yield from next_batches(predictand, next_envelope(content, sheet))
    else:
        for sheet in content:
            yield from next_batches(
                predictand * content[sheet] / sheets,
                next_envelope(content, sheet)
            )


def second_attempt():
    solution = 0
    for envelope in next_batches(1.0, Counter(cut_sheet(A1))):
        solution += envelope.predictand
    print('Solution =', round(solution, 6))


def run_application():
    import time
    start = time.time()
    second_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
