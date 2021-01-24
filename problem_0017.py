"""This solves problem #17 of Project Euler (https://projecteuler.net).

Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3
+ 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when
writing out numbers is in compliance with British usage.
"""


def number_to_digit_list(n):
    return [n // 1000, (n % 1000) // 100, (n % 100) // 10, n % 10]


def ones_word(d):
    w = 'one two three four five six seven eight nine'.split()
    return w[d - 1]


def teen_word(d):
    w = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen ' \
        'nineteen'.split()
    return w[d]


def tens_word(d):
    w = 'twenty thirty forty fifty sixty seventy eighty ninety'.split()
    return w[d - 2]


def first_attempt():
    result = 0
    for n in range(1, 1000 + 1):
        digits = number_to_digit_list(n)
        words = []
        teen = False
        fill = ''
        for i, d in enumerate(digits):
            if i != 3 and d == 0:   # skip nulls if not at ones
                continue
            elif i == 0:    # thousands
                words.append(ones_word(d) + 'thousand')
                fill = 'and'
            elif i == 1:    # hundreds
                words.append(ones_word(d) + 'hundred')
                fill = 'and'
            elif i == 2:    # tens
                if d == 1:
                    teen = True
                    continue
                else:
                    words.append(fill + tens_word(d))
                    fill = ''
            else:   # ones
                if teen:
                    words.append(fill + teen_word(d))
                else:
                    if d == 0:  # skip nulls if at ones, but not teens
                        continue
                    else:
                        words.append(fill + ones_word(d))
        result += len(''.join(words))
    print('result =', result)


def run_application():
    import time
    start = time.time()
    first_attempt()
    print('Runtime =', time.time() - start, 'seconds')


if __name__ == '__main__':
    run_application()

# last line of code
