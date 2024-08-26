import pytest
from day_07 import max_possible_hand


@pytest.mark.parametrize(
    "hand, expected",
    [
        # 0 jacks
        (["2", "2", "K", "3", "3"], ["2", "2", "K", "3", "3"]),
        # 1 jacks
        (["2", "T", "4", "7", "J"], ["2", "T", "4", "7", "T"]),
        (["A", "A", "2", "3", "J"], ["A", "A", "2", "3", "A"]),
        # 2 jacks
        (["J", "J", "5", "7", "6"], ["7", "7", "5", "7", "6"]),
        (["J", "J", "5", "4", "5"], ["5", "5", "5", "4", "5"]),
        (["J", "J", "9", "9", "9"], ["9", "9", "9", "9", "9"]),
        # 3 jacks
        (["J", "J", "5", "J", "6"], ["6", "6", "5", "6", "6"]),
        (["J", "J", "5", "J", "5"], ["5", "5", "5", "5", "5"]),
        # 4 jacks
        (["J", "J", "T", "J", "J"], ["T", "T", "T", "T", "T"]),
        # 5 jacks
        (["J", "J", "J", "J", "J"], ["A", "A", "A", "A", "A"]),
    ],
)
def test_max_possible_hand(hand, expected):
    assert max_possible_hand(hand) == expected
