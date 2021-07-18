from src.pac_man import pac_man_pos, tick, DOT, PAC_MAN, EMPTY


def test_tick_without_state():
    assert tick() == [
        [DOT, DOT, DOT],
        [DOT, PAC_MAN, DOT],
        [DOT, DOT, DOT]
    ]


def test_tick_up():
    assert tick(state=tick(), direction='up') == [
        [DOT, PAC_MAN, DOT],
        [DOT, EMPTY, DOT],
        [DOT, DOT, DOT]
    ]


def test_tick_down():
    assert tick(state=tick(), direction='down') == [
        [DOT, DOT, DOT],
        [DOT, EMPTY, DOT],
        [DOT, PAC_MAN, DOT]
    ]


def test_tick_left():
    assert tick(state=tick(), direction='left') == [
        [DOT, DOT, DOT],
        [PAC_MAN, EMPTY, DOT],
        [DOT, DOT, DOT]
    ]


def test_tick_right():
    assert tick(state=tick(), direction='right') == [
        [DOT, DOT, DOT],
        [DOT, EMPTY, PAC_MAN],
        [DOT, DOT, DOT]
    ]


def test_pac_man_pos():
    assert pac_man_pos(tick()) == [1, 1]
