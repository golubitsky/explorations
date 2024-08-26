from collections import Counter


def O_n_log_n(n):
    if len(n) == 0:
        return 0

    s = sorted(n)
    max_length = 1
    current_length = 1
    last_item = None

    for item in s:
        if last_item and (item == last_item or item == last_item + 1):
            current_length += 1
        else:
            current_length = 1

        last_item = item
        max_length = max(current_length, max_length)

    return max_length


def O_n(n):
    if len(n) == 0:
        return 0

    frequencies = Counter(n)

    max_length = 0

    for value in frequencies:
        current_length = 0
        item = value

        while item in frequencies:
            current_length += frequencies[item]
            item += 1

        max_length = max(current_length, max_length)

    return max_length


def max_tickets(n):
    assert O_n(n) == O_n_log_n(n)
    return O_n_log_n(n)


print(max_tickets([8, 5, 4, 8, 4]) == 3)
print(max_tickets([]) == 0)
print(max_tickets([1]) == 1)
print(max_tickets([1, 2]) == 2)
a = [
    1,
    2,
    5,
    4,
    5,
    6,
]
print(max_tickets(a) == 4)
