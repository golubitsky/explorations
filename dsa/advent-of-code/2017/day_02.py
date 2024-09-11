import re
from itertools import combinations


def part_one(data):
    total = 0

    for line in data:
        n = [int(x) for x in re.findall(r"\d+", line)]
        total += max(n) - min(n)

    print(total)


def part_two(data):
    total = 0

    for line in data:
        n = [int(x) for x in re.findall(r"\d+", line)]
        for a, b in [reversed(sorted(combo)) for combo in combinations(n, 2)]:
            if a // b == a / b:
                total += a // b
                break

    print(total)


if __name__ == "__main__":
    with open("day_02_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
    part_two(data)
