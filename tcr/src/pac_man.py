import copy
import sys

DOT = '.'
EMPTY = ' '
PAC_MAN = '■'
STARTING_STATE = {
    'board': [
        [DOT, DOT, DOT],
        [DOT, PAC_MAN, DOT],
        [DOT, DOT, DOT]
    ],
    'score': 0
}

X_SIZE = 3
Y_SIZE = 3


def wrapped(pos):
    return [
        pos[0] % Y_SIZE,
        pos[1] % X_SIZE
    ]


def up(pos):
    return [pos[0] - 1, pos[1]]


def down(pos):
    return [pos[0] + 1, pos[1]]


def left(pos):
    return [pos[0], pos[1] - 1]


def right(pos):
    return [pos[0], pos[1] + 1]


def next_pos(pos, move):
    return wrapped(
        getattr(sys.modules[__name__], move)(pos)
    )


def tick(state=STARTING_STATE, move=None):
    if move is None:
        return state

    return state_after_move(state, move)


def state_after_move(state, move):
    pos = pac_man_pos(state)

    return next_state(
        state,
        updates=[
            {
                'pos': pos,
                'char': EMPTY
            },
            {
                'pos': next_pos(pos, move),
                'char': PAC_MAN
            }
        ]
    )


def next_state(state, updates):
    next_state = copy.deepcopy(state)

    for update in updates:
        y = update['pos'][0]
        x = update['pos'][1]

        char = next_state['board'][y][x]

        if char == DOT:
            next_state['score'] += 1

        next_state['board'][y][x] = update['char']

    return next_state


def pac_man_pos(state):
    for i, row in enumerate(state['board']):
        for j, cell_content in enumerate(row):
            if cell_content == PAC_MAN:
                return [i, j]
