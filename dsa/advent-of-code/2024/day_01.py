import re
from collections import Counter


def parsed(data):
    numbers = [re.findall(r"\d+", line) for line in data]
    first = []
    second = []
    for a, b in numbers:
        first.append(int(a))
        second.append(int(b))
    return first, second


def part_one(data):
    first, second = parsed(data)

    first.sort()
    second.sort()

    result = 0
    for a, b in zip(first, second):
        result += abs(a - b)

    print(result)


def part_two(data):
    numbers, second = parsed(data)
    frequency = Counter(second)

    result = 0
    for n in numbers:
        result += n * frequency[n]
    print(result)


if __name__ == "__main__":
    with open("day_01_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
    part_two(data)
