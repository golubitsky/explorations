import pytest

from src.pac_man import pac_man_pos, tick, DOT, PAC_MAN, EMPTY


def state_after_moves(moves):
    state = tick()

    for move in moves:
        state = tick(state=state, move=move)

    return state


@pytest.mark.parametrize("moves,expected_board", [
    ([], [[DOT, DOT, DOT],
          [DOT, PAC_MAN, DOT],
          [DOT, DOT, DOT]]),
    (['up'], [
        [DOT, PAC_MAN, DOT],
        [DOT, EMPTY, DOT],
        [DOT, DOT, DOT]]),
    (['down'], [
        [DOT, DOT, DOT],
        [DOT, EMPTY, DOT],
        [DOT, PAC_MAN, DOT]]),
    (['left'], [
        [DOT, DOT, DOT],
        [PAC_MAN, EMPTY, DOT],
        [DOT, DOT, DOT]]),
    (['right'], [
        [DOT, DOT, DOT],
        [DOT, EMPTY, PAC_MAN],
        [DOT, DOT, DOT]])

])
def test_tick_without_state(moves, expected_board):
    assert state_after_moves(moves)['board'] == expected_board


def test_tick_right_wrap_around():
    assert state_after_moves(['right', 'right'])['board'] == [
        [DOT, DOT, DOT],
        [PAC_MAN, EMPTY, EMPTY],
        [DOT, DOT, DOT]
    ]


def test_tick_left_wrap_around():
    assert state_after_moves(['left', 'left'])['board'] == [
        [DOT, DOT, DOT],
        [EMPTY, EMPTY, PAC_MAN],
        [DOT, DOT, DOT]
    ]


def test_tick_up_wrap_around():
    assert state_after_moves(['up', 'up'])['board'] == [
        [DOT, EMPTY, DOT],
        [DOT, EMPTY, DOT],
        [DOT, PAC_MAN, DOT]
    ]


def test_tick_down_wrap_around():
    assert state_after_moves(['down', 'down'])['board'] == [
        [DOT, PAC_MAN, DOT],
        [DOT, EMPTY, DOT],
        [DOT, EMPTY, DOT]
    ]


def test_tick_three_moves():
    assert state_after_moves(['down', 'left', 'up'])['board'] == [
        [DOT, DOT, DOT],
        [PAC_MAN, EMPTY, DOT],
        [EMPTY, EMPTY, DOT]
    ]


def test_tick_score_after_three_moves():
    assert state_after_moves(['down', 'left', 'up'])['score'] == 3


def test_tick_no_score_for_empty():
    assert state_after_moves(['down', 'left', 'up', 'right'])['score'] == 3


def test_pac_man_pos():
    assert pac_man_pos(tick()) == [1, 1]
