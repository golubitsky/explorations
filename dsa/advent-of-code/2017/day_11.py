from collections import Counter


# remainder: {'n': 422, 'ne': 342, 'nw': 99,
#   422 (north)
# + 99  (north "components" of both ne and nw)
# + 243 (342 - 99 of each of the ne/nw "cancel out")
# = 764
# That's the least code I've ever written to solve one of these.
# Although I can't solve part two like this.


def with_direct_cancellation(counter, a, b):
    c = dict(counter)
    m = min(counter[a], counter[b])
    for d in [a, b]:
        c[d] -= m
    return c


def with_diagonal_cancellation(counter, m1, m2, common):
    c = dict(counter)

    m = min(counter[m1], counter[m2])
    if m > 0:
        c[common] += m
        for d in [m1, m2]:
            c[d] -= m

    return c


def with_cancellations(counter):
    counter = with_direct_cancellation(counter, "ne", "sw")
    counter = with_direct_cancellation(counter, "nw", "se")
    counter = with_direct_cancellation(counter, "n", "s")
    counter = with_diagonal_cancellation(counter, "nw", "ne", "n")
    counter = with_diagonal_cancellation(counter, "sw", "se", "s")
    return counter


def part_one(data):
    counts = dict(Counter(data.strip().split(",")))
    print(count_steps_away(dict(counts)))


def count_steps_away(counts):
    return sum(with_cancellations(counts).values())


def part_two(data):
    counts = {
        "se": 0,
        "s": 0,
        "sw": 0,
        "nw": 0,
        "n": 0,
        "ne": 0,
    }

    farthest = 0

    for d in data.split(","):
        counts[d] += 1
        current = count_steps_away(dict(counts))
        if current > farthest:
            farthest = current

    print(farthest)


if __name__ == "__main__":
    with open("day_11_input.txt", "r") as file:
        data = file.read()
    part_one(data)
    part_two(data)  # WIP; 1696 is too high.
