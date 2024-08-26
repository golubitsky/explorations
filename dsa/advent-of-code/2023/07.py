from collections import Counter

CARD_VALUES = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def parsed_hands(data):
    hands = []
    for line in data:
        hand, bid = line.split()
        hand = list(hand)
        bid = int(bid)
        hands.append({"cards": hand, "bid": bid})
    return hands


def is_five_of_a_kind(hand):
    return len(set(hand)) == 1


def is_four_of_a_kind(hand):
    return sorted(list(Counter(hand).values())) == [1, 4]


def is_full_house(hand):
    return sorted(list(Counter(hand).values())) == [2, 3]


def is_three_of_a_kind(hand):
    return sorted(list(Counter(hand).values())) == [1, 1, 3]


def is_two_pair(hand):
    return sorted(list(Counter(hand).values())) == [1, 2, 2]


def is_one_pair(hand):
    return len(set(hand)) == 4


def is_high_card(hand):
    return len(set(hand)) == 5


def camel_sort_fn(hand):
    class_fns = [
        is_five_of_a_kind,
        is_four_of_a_kind,
        is_full_house,
        is_three_of_a_kind,
        is_two_pair,
        is_one_pair,
        is_high_card,
    ]
    class_rank = next((i for i, fn in enumerate(class_fns) if fn(hand["cards"])))

    card_ranks = [-CARD_VALUES.index(c) for c in hand["cards"]]

    return [-class_rank, card_ranks]


def part_one(data):
    parsed = parsed_hands(data)
    parsed.sort(key=camel_sort_fn)

    return sum([rank * hand['bid'] for rank, hand in enumerate(parsed, 1)])
        


if __name__ == "__main__":
    with open("07_input.txt", "r") as file:
        data = file.readlines()
    print(part_one(data))
