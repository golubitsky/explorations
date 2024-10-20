import math
import re
from collections import defaultdict


def min_max(data):
    min_x = math.inf
    min_y = math.inf
    max_x = 0
    max_y = 0

    for x, y in data:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

    return [min_x, min_y, max_x, max_y]


def parsed(data):
    return [tuple([int(x) for x in re.findall(r"\d+", line)]) for line in data]


def potentials(data):
    result = []
    min_x, min_y, max_x, max_y = min_max(data)

    for x, y in data:
        if x in [min_x, max_x] or y in [max_y, min_y]:
            continue
        result.append((x, y))

    return result


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_one(data):
    data = parsed(data)
    min_x, min_y, max_x, max_y = min_max(data)
    closest_area = defaultdict(int)

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = defaultdict(list)

            for pos in data:
                distances[distance((x, y), pos)].append(pos)
            d = min(distances)

            # don't count points equally close to multiple points
            if len(distances[d]) == 1:
                closest_area[distances[d][0]] += 1

    largest_area = 0
    for pos in potentials(data):
        if closest_area[pos] > largest_area:
            largest_area = closest_area[pos]
    print(largest_area)


if __name__ == "__main__":
    with open("day_06_input.txt", "r") as file:
        data = file.readlines()
    part_one(data)
