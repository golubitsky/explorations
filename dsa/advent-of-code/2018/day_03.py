import re
from collections import defaultdict


def part_one(data):
    counts = defaultdict(int)

    for line in data:
        n, x, y, dx, dy = [int(x) for x in re.findall(r"\d+", line)]

        for i_x in range(x, x + dx):
            for i_y in range(y, y + dy):
                counts[(i_x, i_y)] += 1

    print(len([x for x in counts.values() if x >= 2]))


def check(line, patches):
    n, x, y, dx, dy = [int(x) for x in re.findall(r"\d+", line)]

    for i_x in range(x, x + dx):
        for i_y in range(y, y + dy):
            if len(patches[(i_x, i_y)]) > 1:
                return False

    return n


def part_two(data):
    patches = defaultdict(list)

    for line in data:
        n, x, y, dx, dy = [int(x) for x in re.findall(r"\d+", line)]

        for i_x in range(x, x + dx):
            for i_y in range(y, y + dy):
                patches[(i_x, i_y)].append(n)

    for line in data:
        result = check(line, patches)
        if result:
            return result


if __name__ == "__main__":
    with open("day_03_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
    print(part_two(data))
