import re
import sys


KEYS = 'ABCDEFG'

IGNORE_SYMBOLS = set(['||:', ':||', '||', '1.', '2.'])


def letter(symbol):
    return symbol[0].upper()


def accidental(symbol):
    accidental_found = re.search(r'#|b', symbol)
    return accidental_found.group(0) if accidental_found else ''


def quality(symbol):
    return re.search(r'(\w[#|b]*)(.*)', symbol).group(2)


def one_letter_up(letter):
    return KEYS[(KEYS.find(letter) + 1) % len(KEYS)]


def transposed(symbol):
    if symbol in IGNORE_SYMBOLS:
        return symbol

    if accidental(symbol) == 'b':
        if letter(symbol) in 'BEADG':
            return f'{letter(symbol)}{quality(symbol)}'
        else:
            raise NotImplementedError(symbol)
    if accidental(symbol) == '#':
        if letter(symbol) in 'GCFDA':
            return f'{one_letter_up(letter(symbol))}{quality(symbol)}'
        else:
            raise NotImplementedError(symbol)

    if letter(symbol) in 'GCF':
        return f'{letter(symbol)}#{quality(symbol)}'
    elif letter(symbol) in 'DA':
        # prefer flats for now
        return f'{one_letter_up(letter(symbol))}b{quality(symbol)}'
    else:
        return f'{one_letter_up(letter(symbol))}{quality(symbol)}'


def transposed_line(line):
    return [transposed(symbol) for symbol in line]


def tune_transposed_up_half_step(lines_of_chords):
    return [transposed_line(line) for line in lines_of_chords]


def lines_of_chords(filename):
    with open(filename) as file:
        return [line.split() for line in list(file)]


if __name__ == '__main__':
    lines = lines_of_chords(f'tunes/{sys.argv[1]}')
    for line in tune_transposed_up_half_step(lines):
        print(' '.join(line))
