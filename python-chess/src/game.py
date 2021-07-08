from termcolor import cprint

WHITE = 'w'
BLACK = 'b'

CHARS = {
    BLACK: {
        'checker': u'\u25FB',
        'pawn': u'\u265F',
        'rook': u'\u265C',
        'knight': u'\u265E',
        'bishop': u'\u265D',
        'king': u'\u265A',
        'queen': u'\u265B',
    },
    WHITE: {
        'checker': u'\u25FC',
        'pawn': u'\u2659',
        'rook': u'\u2656',
        'knight': u'\u2658',
        'bishop': u'\u2657',
        'king': u'\u2654',
        'queen': u'\u2655'
    }
}

PAWNS = ['pawn' for x in range(8)]
PIECES = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
BLANK_ROW = [' ' for x in range(8)]

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8']

STARTING_POSITION = [
    [CHARS[BLACK][piece] for piece in PIECES],
    [CHARS[BLACK][pawn] for pawn in PAWNS],
    BLANK_ROW,
    BLANK_ROW,
    BLANK_ROW,
    BLANK_ROW,
    [CHARS[WHITE][pawn] for pawn in PAWNS],
    [CHARS[WHITE][piece] for piece in PIECES],
]


def print_on_grey(x): return cprint(x, 'white', 'on_grey', end=' ')


def print_on_white(x): return cprint(x, 'white', 'on_white', end=' ')


def print_function(number_index, letter_index):
    if number_index % 2 == 0:
        return print_on_grey if letter_index % 2 == 0 else print_on_white
    else:
        return print_on_white if letter_index % 2 == 0 else print_on_grey


def print_board(position):
    for number_index, number in enumerate(reversed(NUMBERS)):
        print(number, end='  ')

        for letter_index, letter in enumerate(LETTERS):
            fn = print_function(number_index, letter_index)
            fn(position[number_index][letter_index])
        print()

    print()
    print('   ' + ' '.join(LETTERS))


if __name__ == '__main__':
    print_board(STARTING_POSITION)
