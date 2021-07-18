import copy
import sys

DOT = '.'
EMPTY = ' '
PAC_MAN = '■'
STARTING_STATE = [
    [DOT, DOT, DOT],
    [DOT, PAC_MAN, DOT],
    [DOT, DOT, DOT]
]


def up(pos):
    return [pos[0] - 1, pos[1]]


def down(pos):
    return [pos[0] + 1, pos[1]]


def left(pos):
    return [pos[0], pos[1] - 1]


def right(pos):
    return [pos[0], pos[1] + 1]


def next_pos(pos, direction):
    return getattr(sys.modules[__name__], direction)(pos)


def tick(state=STARTING_STATE, direction=None):
    if direction is None:
        return state

    return move(state, direction)


def move(state, direction):
    pos = pac_man_pos(state)

    return next_state(
        state,
        updates=[
            {
                'pos': pos,
                'char': EMPTY
            },
            {
                'pos': next_pos(pos, direction),
                'char': PAC_MAN
            }
        ]
    )


def next_state(state, updates):
    next_state = copy.deepcopy(state)

    for update in updates:
        next_state[update['pos'][0]][update['pos'][1]] = update['char']

    return next_state


def pac_man_pos(state):
    for i, row in enumerate(state):
        for j, cell_content in enumerate(row):
            if cell_content == PAC_MAN:
                return [i, j]
